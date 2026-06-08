import random
import tkinter as tk
from tkinter import messagebox

#  WORD BANK  (Easy / Medium / Hard)

WORD_BANK = {
    "easy": [
        ("cat",      "A common pet that meows"),
        ("dog",      "Man's best friend"),
        ("sun",      "The star at the center of our solar system"),
        ("book",     "You read this"),
        ("fish",     "Lives in water"),
    ],
    "medium": [
        ("python",   "A popular programming language"),
        ("hangman",  "The game you are playing right now"),
        ("science",  "Study of the natural world"),
        ("keyboard", "You type on this"),
        ("laptop",   "A portable computer"),
    ],
    "hard": [
        ("algorithm",    "Step-by-step problem-solving procedure"),
        ("cryptocurrency","Digital or virtual currency"),
        ("photosynthesis","How plants make food from sunlight"),
        ("onomatopoeia", "A word that imitates a sound"),
        ("bureaucracy",  "Complex system of rules and procedures"),
    ],
}

MAX_WRONG = {"easy": 8, "medium": 6, "hard": 4}

STAGES = [
    # 0 wrong
    """
   -----
   |   |
       |
       |
       |
       |
=========""",
    # 1
    """
   -----
   |   |
   O   |
       |
       |
       |
=========""",
    # 2
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========""",
    # 3
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========""",
    # 4
    r"""
   -----
   |   |
   O   |
  /|\  |
       |
       |
=========""",
    # 5
    r"""
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
=========""",
    # 6  (game-over for medium)
    r"""
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
========="""
]

# extra stages for easy (7 & 8 wrong)
EXTRA_STAGES = [
    r"""
   -----
   |   |
  \O   |
  /|\  |
  / \  |
       |
=========""",
    r"""
   -----
   |   |
  \O/  |
  /|\  |
  / \  |
       |
========="""
]

ALL_STAGES = STAGES + EXTRA_STAGES   # indices 0-8


def get_stage(wrong, difficulty):
    max_w = MAX_WRONG[difficulty]
    # map wrong count to 0-6 range proportionally
    idx = round((wrong / max_w) * 6)
    return STAGES[min(idx, 6)]


def display_word(word, guessed):
    return " ".join(c if c in guessed else "_" for c in word)


#  CONSOLE  VERSION  (single & multiplayer)

def choose_difficulty():
    print("\nChoose difficulty:")
    print("  1. Easy   (8 wrong allowed, longer words suggested)")
    print("  2. Medium (6 wrong allowed)")
    print("  3. Hard   (4 wrong allowed, tough words)")
    choice = input("Enter 1 / 2 / 3: ").strip()
    return {"1": "easy", "2": "medium", "3": "hard"}.get(choice, "medium")


def play_round_console(word, hint, difficulty, player_name=""):
    guessed = set()
    wrong   = 0
    max_w   = MAX_WRONG[difficulty]
    hints_left = 1                        # one free hint per round

    prefix = f"[{player_name}] " if player_name else ""
    print(f"\n{prefix}Word has {len(word)} letters.  Difficulty: {difficulty.upper()}")
    print(f"Wrong guesses allowed: {max_w}")

    while True:
        print(get_stage(wrong, difficulty))
        current = display_word(word, guessed)
        print(f"\nWord:    {current}")
        print(f"Guessed: {', '.join(sorted(guessed)) or 'None'}")
        print(f"Wrong left: {max_w - wrong}   |   Hints left: {hints_left}")

        if "_" not in current:
            print(f"\n{prefix}You won! The word was: {word.upper()}")
            return True

        if wrong >= max_w:
            print(f"\n{prefix}Game over! The word was: {word.upper()}")
            return False

        action = input("\nGuess a letter (or type 'hint'): ").lower().strip()

        if action == "hint":
            if hints_left > 0:
                hints_left -= 1
                print(f"Hint: {hint}")
            else:
                print("No hints left!")
            continue

        if len(action) != 1 or not action.isalpha():
            print("Please enter a single letter.")
            continue
        if action in guessed:
            print(f"Already guessed '{action}'.")
            continue

        guessed.add(action)
        if action in word:
            print(f"'{action}' is in the word!")
        else:
            wrong += 1
            print(f"'{action}' is NOT in the word.")


def singleplayer_console():
    difficulty = choose_difficulty()
    wins = losses = 0
    while True:
        word, hint = random.choice(WORD_BANK[difficulty])
        if play_round_console(word, hint, difficulty):
            wins += 1
        else:
            losses += 1
        print(f"\nScore  —  Wins: {wins}   Losses: {losses}")
        if input("Play again? (y/n): ").lower().strip() != "y":
            break


def multiplayer_console():
    """Two players take turns guessing the same set of words."""
    difficulty = choose_difficulty()
    rounds = int(input("How many rounds? ").strip() or "3")

    p1 = input("Player 1 name: ").strip() or "Player 1"
    p2 = input("Player 2 name: ").strip() or "Player 2"
    scores = {p1: 0, p2: 0}

    for r in range(1, rounds + 1):
        print(f"\n{'='*40}")
        print(f"  ROUND {r} of {rounds}")
        print(f"{'='*40}")
        word, hint = random.choice(WORD_BANK[difficulty])

        for player in [p1, p2]:
            input(f"\n{player}'s turn — press Enter when ready...")
            won = play_round_console(word, hint, difficulty, player_name=player)
            if won:
                scores[player] += 1

    print("\n===== FINAL SCORES =====")
    for player, score in sorted(scores.items(), key=lambda x: -x[1]):
        print(f"  {player}: {score} win(s)")
    winner = max(scores, key=scores.get)
    if scores[p1] == scores[p2]:
        print("It's a tie!")
    else:
        print(f"Winner: {winner}!")


#  TKINTER  GUI  VERSION

class HangmanGUI:
    GALLOWS = [
        # stage 0-6 as lists of canvas draw calls (line coords)
        # We'll draw programmatically
    ]

    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.resizable(False, False)
        self.root.configure(bg="#f8f8f2")

        self.difficulty = tk.StringVar(value="medium")
        self.mode       = tk.StringVar(value="single")
        self.word       = ""
        self.hint       = ""
        self.guessed    = set()
        self.wrong      = 0
        self.max_wrong  = 6
        self.hints_left = 1
        self.game_active= False

        # multiplayer state
        self.players    = []
        self.cur_player = 0
        self.mp_scores  = {}
        self.mp_round   = 0
        self.mp_rounds  = 3

        self._build_ui()
        self._new_game()

    # ── UI construction ──────────────────────────────

    def _build_ui(self):
        top = tk.Frame(self.root, bg="#f8f8f2", pady=8)
        top.pack(fill="x", padx=16)

        # Mode selector
        tk.Label(top, text="Mode:", bg="#f8f8f2", font=("Helvetica", 11)).pack(side="left")
        for m, label in [("single", "Single"), ("multi", "Multiplayer")]:
            tk.Radiobutton(top, text=label, variable=self.mode, value=m,
                           bg="#f8f8f2", font=("Helvetica", 11),
                           command=self._new_game).pack(side="left", padx=4)

        tk.Label(top, text="  Difficulty:", bg="#f8f8f2", font=("Helvetica", 11)).pack(side="left")
        for d, label in [("easy","Easy"), ("medium","Medium"), ("hard","Hard")]:
            tk.Radiobutton(top, text=label, variable=self.difficulty, value=d,
                           bg="#f8f8f2", font=("Helvetica", 11),
                           command=self._new_game).pack(side="left", padx=2)

        # Canvas for gallows
        self.canvas = tk.Canvas(self.root, width=200, height=220,
                                bg="#f8f8f2", highlightthickness=0)
        self.canvas.pack(pady=(4, 0))

        # Word display
        self.word_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.word_var, font=("Courier", 26, "bold"),
                 bg="#f8f8f2", fg="#282a36", letter_spacing=4).pack(pady=8)

        # Status bar
        self.status_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.status_var, font=("Helvetica", 12),
                 bg="#f8f8f2", fg="#6272a4").pack()

        # Hint button
        self.hint_btn = tk.Button(self.root, text="Use Hint",
                                  font=("Helvetica", 11), command=self._use_hint,
                                  bg="#bd93f9", fg="white", relief="flat",
                                  padx=10, pady=4, cursor="hand2")
        self.hint_btn.pack(pady=4)

        # Keyboard
        kb_frame = tk.Frame(self.root, bg="#f8f8f2")
        kb_frame.pack(pady=8, padx=16)
        self.key_buttons = {}
        for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz"):
            row, col = divmod(i, 9)
            btn = tk.Button(kb_frame, text=ch.upper(), width=3,
                            font=("Helvetica", 11, "bold"),
                            bg="#44475a", fg="white", relief="flat",
                            activebackground="#6272a4",
                            command=lambda c=ch: self._guess(c),
                            cursor="hand2")
            btn.grid(row=row, column=col, padx=3, pady=3)
            self.key_buttons[ch] = btn

        # Player label (multiplayer)
        self.player_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.player_var,
                 font=("Helvetica", 13, "bold"), bg="#f8f8f2", fg="#ff79c6").pack()

        # Score label
        self.score_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.score_var,
                 font=("Helvetica", 11), bg="#f8f8f2", fg="#50fa7b").pack(pady=2)

        # New game button
        tk.Button(self.root, text="New Game", font=("Helvetica", 11),
                  command=self._new_game, bg="#50fa7b", fg="#282a36",
                  relief="flat", padx=10, pady=4, cursor="hand2").pack(pady=8)

    # ── Game logic ───────────────────────────────────

    def _new_game(self):
        diff = self.difficulty.get()
        self.max_wrong  = MAX_WRONG[diff]
        self.word, self.hint = random.choice(WORD_BANK[diff])
        self.guessed    = set()
        self.wrong      = 0
        self.hints_left = 1
        self.game_active= True

        if self.mode.get() == "multi" and not self.players:
            self._setup_multiplayer()

        self._reset_keys()
        self._update_ui()

    def _setup_multiplayer(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("Multiplayer Setup")
        dlg.configure(bg="#f8f8f2")
        dlg.grab_set()

        tk.Label(dlg, text="Player 1 name:", bg="#f8f8f2").grid(row=0, column=0, padx=8, pady=4)
        p1e = tk.Entry(dlg); p1e.insert(0, "Player 1"); p1e.grid(row=0, column=1, padx=8)

        tk.Label(dlg, text="Player 2 name:", bg="#f8f8f2").grid(row=1, column=0, padx=8, pady=4)
        p2e = tk.Entry(dlg); p2e.insert(0, "Player 2"); p2e.grid(row=1, column=1, padx=8)

        tk.Label(dlg, text="Rounds:", bg="#f8f8f2").grid(row=2, column=0, padx=8, pady=4)
        re = tk.Entry(dlg, width=5); re.insert(0, "3"); re.grid(row=2, column=1, sticky="w", padx=8)

        def confirm():
            self.players    = [p1e.get() or "P1", p2e.get() or "P2"]
            self.mp_rounds  = int(re.get() or 3)
            self.mp_round   = 1
            self.cur_player = 0
            self.mp_scores  = {p: 0 for p in self.players}
            dlg.destroy()

        tk.Button(dlg, text="Start", command=confirm,
                  bg="#50fa7b", fg="#282a36", relief="flat",
                  padx=10, pady=4).grid(row=3, column=0, columnspan=2, pady=8)
        self.root.wait_window(dlg)

    def _guess(self, ch):
        if not self.game_active or ch in self.guessed:
            return
        self.guessed.add(ch)
        btn = self.key_buttons[ch]
        if ch in self.word:
            btn.configure(bg="#50fa7b", fg="#282a36")
        else:
            self.wrong += 1
            btn.configure(bg="#ff5555", fg="white")
        self._update_ui()
        self._check_end()

    def _use_hint(self):
        if self.hints_left > 0 and self.game_active:
            self.hints_left -= 1
            messagebox.showinfo("Hint", self.hint)
            self._update_ui()

    def _check_end(self):
        current = display_word(self.word, self.guessed)
        won  = "_" not in current
        lost = self.wrong >= self.max_wrong

        if not (won or lost):
            return

        self.game_active = False

        if won:
            msg = f"You got it!\nThe word was: {self.word.upper()}"
        else:
            msg = f"Game over!\nThe word was: {self.word.upper()}"

        if self.mode.get() == "multi" and self.players:
            player = self.players[self.cur_player]
            if won:
                self.mp_scores[player] += 1

            messagebox.showinfo("Round result", f"{player}: {msg}")

            # Next player's turn
            next_p = (self.cur_player + 1) % len(self.players)
            if next_p != 0:
                self.cur_player = next_p
                self.guessed    = set()
                self.wrong      = 0
                self.hints_left = 1
                self.game_active= True
                self._reset_keys()
                self._update_ui()
                messagebox.showinfo("Next turn",
                    f"{self.players[self.cur_player]}'s turn!\nClose this dialog to begin.")
            else:
                self.mp_round += 1
                if self.mp_round > self.mp_rounds:
                    # Show final scores
                    score_str = "\n".join(
                        f"{p}: {s} win(s)" for p, s in
                        sorted(self.mp_scores.items(), key=lambda x: -x[1])
                    )
                    winner = max(self.mp_scores, key=self.mp_scores.get)
                    tied   = len(set(self.mp_scores.values())) == 1
                    result = "It's a tie!" if tied else f"Winner: {winner}!"
                    messagebox.showinfo("Game Over", f"Final Scores:\n{score_str}\n\n{result}")
                    self.players = []       # reset for fresh setup next time
                    self._new_game()
                else:
                    self.cur_player = 0
                    self._new_game()
        else:
            messagebox.showinfo("Result", msg)

    # ── Drawing ──────────────────────────────────────

    def _draw_gallows(self):
        c = self.canvas
        c.delete("all")
        # base & pole
        c.create_line(20, 210, 180, 210, width=4, fill="#44475a")  # base
        c.create_line(60,  10,  60, 210, width=4, fill="#44475a")  # pole
        c.create_line(60,  10, 140,  10, width=4, fill="#44475a")  # top
        c.create_line(140, 10, 140,  40, width=4, fill="#44475a")  # rope

        w = self.wrong
        max_w = self.max_wrong
        # proportional body parts (scale to difficulty)
        show = lambda n: w >= round((n / 6) * max_w)

        if show(1):   # head
            c.create_oval(120, 40, 160, 80, width=3, outline="#ff5555")
        if show(2):   # body
            c.create_line(140, 80, 140, 140, width=3, fill="#ff5555")
        if show(3):   # left arm
            c.create_line(140, 95, 110, 120, width=3, fill="#ff5555")
        if show(4):   # right arm
            c.create_line(140, 95, 170, 120, width=3, fill="#ff5555")
        if show(5):   # left leg
            c.create_line(140, 140, 110, 175, width=3, fill="#ff5555")
        if show(6):   # right leg
            c.create_line(140, 140, 170, 175, width=3, fill="#ff5555")

    def _reset_keys(self):
        for btn in self.key_buttons.values():
            btn.configure(bg="#44475a", fg="white", state="normal")

    def _update_ui(self):
        self._draw_gallows()
        self.word_var.set(display_word(self.word, self.guessed))
        self.status_var.set(
            f"Wrong: {self.wrong}/{self.max_wrong}   |   "
            f"Difficulty: {self.difficulty.get().capitalize()}   |   "
            f"Hints left: {self.hints_left}"
        )
        self.hint_btn.configure(
            state="normal" if self.hints_left > 0 and self.game_active else "disabled"
        )
        if self.mode.get() == "multi" and self.players:
            self.player_var.set(
                f"{self.players[self.cur_player]}'s turn  —  "
                f"Round {self.mp_round}/{self.mp_rounds}"
            )
            score_str = "   ".join(f"{p}: {s}" for p, s in self.mp_scores.items())
            self.score_var.set(f"Scores: {score_str}")
        else:
            self.player_var.set("")
            self.score_var.set("")


#  MAIN  MENU

def main():
    print("\n╔══════════════════════════════╗")
    print("║       HANGMAN  GAME          ║")
    print("╠══════════════════════════════╣")
    print("║  1. Single-player (console)  ║")
    print("║  2. Multiplayer  (console)   ║")
    print("║  3. GUI  (Tkinter)           ║")
    print("║  4. Exit                     ║")
    print("╚══════════════════════════════╝")

    choice = input("Choose mode: ").strip()

    if choice == "1":
        singleplayer_console()
    elif choice == "2":
        multiplayer_console()
    elif choice == "3":
        root = tk.Tk()
        HangmanGUI(root)
        root.mainloop()
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        master.title("Flashcard Application")
        master.configure(bg='#E8EAE6')  # Set a neutral background color

        self.flashcards = {
            "What Is The Symbol of Copper ?": "Cu",
            "What Is The Atomic Number of Aluminum ?": "13",
            "What Is The Common Name of CH4 ?": "Methane",
            "What is the formula of sulfuric acid ?": "H2SO4",
            "How Many Atoms are there in the compound CaCO3 ?": "5",
            "How Many Electrons are in the s orbital ?": "2",
            "1 atm of Pressure equals how many mmHg ?": "760"
        }
        self.total_flashcards = len(self.flashcards)
        self.current_flashcard_index = 0
        self.correct_answers = 0

        self.flashcard_label = tk.Label(master, text="", font=("Arial", 16, 'bold'), bg='#E8EAE6')
        self.flashcard_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=("Arial", 14), justify='center')
        self.answer_entry.pack(pady=10)

        self.check_answer_button = tk.Button(master, text="Check Answer", command=self.check_answer, bg='#A7BEA9', fg='white')
        self.check_answer_button.pack(pady=10)

        self.feedback_label = tk.Label(master, text="", font=("Arial", 12), bg='#E8EAE6')
        self.feedback_label.pack(pady=5)

        self.score_label = tk.Label(master, text="Score: 0", font=("Arial", 12), bg='#E8EAE6')
        self.score_label.pack(pady=5)

        self.button_frame = tk.Frame(master, bg='#E8EAE6')
        self.button_frame.pack(pady=10)

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.show_previous_flashcard, bg='#A7BEA9', fg='white')
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.show_next_flashcard, bg='#A7BEA9', fg='white')
        self.next_button.pack(side=tk.LEFT, padx=10)

        self.show_flashcard()  # Start with the first card

    def show_flashcard(self):
        if self.current_flashcard_index < self.total_flashcards:
            current_card = list(self.flashcards.items())[self.current_flashcard_index]
            self.flashcard_label.config(text=current_card[0])
            self.answer_entry.delete(0, tk.END)  # Clear answer entry
            self.feedback_label.config(text="")
            self.check_answer_button.config(state=tk.NORMAL)  # Enable button for new question
        else:
            messagebox.showinfo("Flashcards Finished", "You have finished all flashcards!")

    def show_next_flashcard(self):
        self.current_flashcard_index += 1
        self.show_flashcard()

    def show_previous_flashcard(self):
        self.current_flashcard_index = max(0, self.current_flashcard_index - 1)
        self.show_flashcard()

    def check_answer(self):
        answer = self.answer_entry.get().strip().lower()
        correct_answer = list(self.flashcards.values())[self.current_flashcard_index].strip().lower()
        if answer == correct_answer:
            self.feedback_label.config(text="Correct!", fg='green')
            self.correct_answers += 1
            self.score_label.config(text=f"Score: {self.correct_answers}")
        else:
            self.feedback_label.config(text=f"Incorrect. The correct answer is: {correct_answer}", fg='red')
        self.check_answer_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    root.geometry("500x400")
    app = FlashcardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

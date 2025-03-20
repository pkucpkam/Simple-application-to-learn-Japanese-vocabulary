import random
import tkinter as tk

# Bảng Hiragana và Romaji tương ứng, bao gồm cả các ký tự ghép
hiragana_romaji = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n',

    # Các ký tự ghép
    'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
    'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
    'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
    'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
    'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
    'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
    'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
    
    'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
    'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
    'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
    'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo'
}

class HiraganaQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hiragana Quiz")
        
        self.root.geometry("400x600")
        
        self.streak = 0
        
        self.hiragana_label = tk.Label(root, text="Chữ cái Hiragana: ", font=("Helvetica", 16))
        self.hiragana_label.pack(pady=20)
        
        self.hiragana_char = tk.Label(root, text="", font=("Helvetica", 24), width=10)
        self.hiragana_char.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.streak_label = tk.Label(root, text=f"Streak: {self.streak} ", font=("Helvetica", 16))
        self.streak_label.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Tiếp tục", font=("Helvetica", 14), command=self.next_question)
        self.next_button.pack(pady=10)

        self.next_question()

        self.entry.bind("<Return>", self.check_answer) 

    def next_question(self):
        self.hiragana_char.config(text=random.choice(list(hiragana_romaji.keys())))
        self.entry.delete(0, tk.END)  

    def check_answer(self, event=None):
        hiragana = self.hiragana_char.cget("text")
        correct_romaji = hiragana_romaji[hiragana]
        user_input = self.entry.get().lower()

        if user_input == correct_romaji:
            self.result_label.config(text="Chính xác!", fg="green")
            self.streak += 1 
        else:
            self.result_label.config(text=f"Sai rồi! Phiên âm đúng là: {correct_romaji}", fg="red")
            self.streak = 0 

        self.streak_label.config(text=f"Streak: {self.streak}")

        self.next_question()

# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = HiraganaQuizApp(root)
    root.mainloop()

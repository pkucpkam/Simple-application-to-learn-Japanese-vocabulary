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

katakana_romaji = {
    'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
    'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
    'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',
    'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
    'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',
    'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
    'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo',
    'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
    'ワ': 'wa', 'ヲ': 'wo', 'ン': 'n',
    # Các ký tự ghép
    'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo',
    'シャ': 'sha', 'シュ': 'shu', 'ショ': 'sho',
    'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho',
    'ニャ': 'nya', 'ニュ': 'nyu', 'ニョ': 'nyo',
    'ヒャ': 'hya', 'ヒュ': 'hyu', 'ヒョ': 'hyo',
    'ミャ': 'mya', 'ミュ': 'myu', 'ミョ': 'myo',
    'リャ': 'rya', 'リュ': 'ryu', 'リョ': 'ryo',
    'ギャ': 'gya', 'ギュ': 'gyu', 'ギョ': 'gyo',
    'ジャ': 'ja', 'ジュ': 'ju', 'ジョ': 'jo',
    'ビャ': 'bya', 'ビュ': 'byu', 'ビョ': 'byo',
    'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo'
}

class HiraganaKatakanaQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hiragana & Katakana Quiz")
        
        self.root.geometry("400x600")
        
        self.streak = 0
        self.selected_type = None
        
        # Trang chủ
        self.title_label = tk.Label(root, text="Chọn bảng chữ: ", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        self.hiragana_button = tk.Button(root, text="Hiragana", font=("Helvetica", 14), command=self.select_hiragana)
        self.hiragana_button.pack(pady=10)

        self.katakana_button = tk.Button(root, text="Katakana", font=("Helvetica", 14), command=self.select_katakana)
        self.katakana_button.pack(pady=10)

    def select_hiragana(self):
        self.selected_type = "hiragana"
        self.initialize_quiz()

    def select_katakana(self):
        self.selected_type = "katakana"
        self.initialize_quiz()

    def initialize_quiz(self):
        # Ẩn các phần tử trang chủ
        self.title_label.pack_forget()
        self.hiragana_button.pack_forget()
        self.katakana_button.pack_forget()

        # Hiển thị các phần tử của trang quiz
        self.hiragana_label = tk.Label(self.root, text="Chữ cái: ", font=("Helvetica", 16))
        self.hiragana_label.pack(pady=20)

        self.hiragana_char = tk.Label(self.root, text="", font=("Helvetica", 24), width=10)
        self.hiragana_char.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.entry.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.streak_label = tk.Label(self.root, text=f"Streak: {self.streak} ", font=("Helvetica", 16))
        self.streak_label.pack(pady=10)

        self.next_button = tk.Button(self.root, text="Tiếp tục", font=("Helvetica", 14), command=self.next_question)
        self.next_button.pack(pady=10)

        # Thêm nút quay lại trang chủ
        self.back_button = tk.Button(self.root, text="Quay lại trang chủ", font=("Helvetica", 14), command=self.back_to_home)
        self.back_button.pack(pady=10)

        self.entry.bind("<Return>", self.check_answer)

        self.next_question()

    def next_question(self):
        if self.selected_type == "hiragana":
            self.hiragana_char.config(text=random.choice(list(hiragana_romaji.keys())))
            self.current_set = hiragana_romaji
        else:
            self.hiragana_char.config(text=random.choice(list(katakana_romaji.keys())))
            self.current_set = katakana_romaji
        
        self.entry.delete(0, tk.END)

    def check_answer(self, event=None):
        character = self.hiragana_char.cget("text")
        correct_romaji = self.current_set[character]
        user_input = self.entry.get().lower()

        if user_input == correct_romaji:
            self.result_label.config(text="Chính xác!", fg="green")
            self.streak += 1
        else:
            self.result_label.config(text=f"Sai rồi! Phiên âm đúng là: {correct_romaji}", fg="red")
            self.streak = 0

        self.streak_label.config(text=f"Streak: {self.streak}")

        self.next_question()

    def back_to_home(self):
        # Ẩn các phần tử quiz
        self.hiragana_label.pack_forget()
        self.hiragana_char.pack_forget()
        self.entry.pack_forget()
        self.result_label.pack_forget()
        self.streak_label.pack_forget()
        self.next_button.pack_forget()
        self.back_button.pack_forget()

        # Reset streak
        self.streak = 0

        # Hiển thị lại trang chủ
        self.title_label.pack(pady=20)
        self.hiragana_button.pack(pady=10)
        self.katakana_button.pack(pady=10)

# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = HiraganaKatakanaQuizApp(root)
    root.mainloop()

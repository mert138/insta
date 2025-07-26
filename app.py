from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        kullanici_adi = request.form["username"]
        sifre = request.form["password"]

        with open("kullanicilar.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"Kullanıcı: {kullanici_adi} | Şifre: {sifre}\n")

        return f"<h2>Hoş geldin {kullanici_adi}! Giriş kaydedildi.</h2>"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

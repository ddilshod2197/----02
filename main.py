class Arxitektor:
    def __init__(self, ism, familiya, tajriba):
        self.ism = ism
        self.familiya = familiya
        self.tajriba = tajriba

    def ishlaydi(self):
        return f"{self.ism} {self.familiya} ishlaydi."

class Google:
    def __init__(self, arxitektor):
        self.arxitektor = arxitektor

    def ishlaydi(self):
        return f"Google: {self.arxitektor.ishlaydi()}"

class Meta:
    def __init__(self, arxitektor):
        self.arxitektor = arxitektor

    def ishlaydi(self):
        return f"Meta: {self.arxitektor.ishlaydi()}"

arxitektor = Arxitektor("Ali", "Valiyev", "Google va Meta tajribasi")
google = Google(arxitektor)
meta = Meta(arxitektor)

print(google.ishlaydi())
print(meta.ishlaydi())

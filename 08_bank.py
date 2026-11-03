class RBI:
    def get_interest(self):
        return 6


class SBI(RBI):
    def get_interest(self):
        return super().get_interest() + 1


class HDFC(RBI):
    def get_interest(self):
        return super().get_interest() + 2
    
class BOB(RBI):
    def get_interest(self):
        return super().get_interest() + 5


sbi = SBI()
hdfc = HDFC()
bob = BOB()

print("SBI interest:", sbi.get_interest(), "%")
print("HDFC interest:", hdfc.get_interest(), "%")
print("BOB interest:", bob.get_interest(), "%")
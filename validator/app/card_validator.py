class CardValidator:
    def __init__(self, card_number):
        self.card_number = card_number

    def is_valid(self):
        return self.luhn_check(self.card_number)

    def luhn_check(self, card_number):
        total = 0
        reverse_digits = card_number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    def identify_card_type(self, card_number):
        if not self.is_valid():
            return "Invalid card number"
        
        if self.card_number.startswith('4'):
            return "Visa"
        elif self.card_number.startswith(('51', '52', '53', '54', '55')):
            return "MasterCard"
        elif self.card_number.startswith('34') or self.card_number.startswith('37'):
            return "American Express"
        elif self.card_number.startswith('6011') or self.card_number.startswith('65'):
            return "Discover"
        elif self.card_number.startswith('5012') or self.card_number.startswith('5013'):
            return "Diners Club"
        elif self.card_number.startswith('5018'):
            return "Maestro"
        elif self.card_number.startswith('5019'):
            return "Elo"
        elif self.card_number.startswith('5067') or self.card_number.startswith('5068'):
            return "Hipercard"
        elif self.card_number.startswith('6363'):
            return "Aura"
        elif self.card_number.startswith('6361'):
            return "JCB"
        elif self.card_number.startswith('6360'):
            return "UnionPay"
        elif self.card_number.startswith('6026'):
            return "Edenred"
        elif self.card_number.startswith('5019'):
            return "Sodexo"
        elif self.card_number.startswith('6362'):
            return "Ticket"
        elif self.card_number.startswith('637'):    
            return "Vale"   
        else:
            return "Unknown card type"
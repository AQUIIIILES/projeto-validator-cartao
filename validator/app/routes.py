from flask import Blueprint, request, jsonify, render_template
from .card_validator import CardValidator

bp = Blueprint('routes', __name__)

@bp.route('/validate', methods=['POST'])
def validate_card():
    card_number = request.form.get('card_number')
    
    validator = CardValidator(card_number)
    card_type = validator.identify_card_type(card_number)

    if card_type != "Invalid card number":
        return render_template('index.html', card_type=card_type)
    else:
        return render_template('index.html', error='Invalid card number')

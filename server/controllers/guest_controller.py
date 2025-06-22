from flask import Blueprint, request, jsonify
from models import db, Guest

guest_bp = Blueprint('guests', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    try:
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
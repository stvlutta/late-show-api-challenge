from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Appearance, Guest, Episode

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    try:
        data = request.get_json()
        
        if not data or not all(key in data for key in ['rating', 'guest_id', 'episode_id']):
            return jsonify({'error': 'Rating, guest_id, and episode_id are required'}), 400
        
        guest = Guest.query.get(data['guest_id'])
        if not guest:
            return jsonify({'error': 'Guest not found'}), 404
        
        episode = Episode.query.get(data['episode_id'])
        if not episode:
            return jsonify({'error': 'Episode not found'}), 404
        
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        
        db.session.add(appearance)
        db.session.commit()
        
        return jsonify(appearance.to_dict()), 201
        
    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
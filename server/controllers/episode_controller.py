from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Episode, Appearance

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    try:
        episodes = Episode.query.all()
        return jsonify([episode.to_dict() for episode in episodes]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    try:
        episode = Episode.query.get_or_404(id)
        episode_data = episode.to_dict()
        
        appearances = Appearance.query.filter_by(episode_id=id).all()
        episode_data['appearances'] = [appearance.to_dict() for appearance in appearances]
        
        return jsonify(episode_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    try:
        episode = Episode.query.get_or_404(id)
        db.session.delete(episode)
        db.session.commit()
        
        return jsonify({'message': 'Episode deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
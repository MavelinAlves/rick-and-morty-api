from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/character', methods=['POST'])
def get_character():
    data = request.get_json()

    if not data or 'character_id' not in data:
        return jsonify({"error": "Invalid request. Please provide a character_id."}), 400

    character_id = data['character_id']

    try:
        # Consumir la API de Rick and Morty
        api_url = f"https://rickandmortyapi.com/api/character/{character_id}"
        response = requests.get(api_url)

        if response.status_code == 404:
            return jsonify({"error": "Character not found"}), 404

        character_data = response.json()
        name = character_data.get("name")
        status = character_data.get("status")

        return jsonify({
            "name": name,
            "status": status
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Error while trying to reach the Rick and Morty API"}), 500

if __name__ == '__main__':
    app.run(debug=True)

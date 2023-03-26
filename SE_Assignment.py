import unittest
from flask import Flask, jsonify
app = Flask(__name__)
class CulturalDestination:
    def __init__(self, city, visual_art_space, public_art, programming, talent_platform):
        self.city = city
        self.visual_art_space = visual_art_space
        self.public_art = public_art
        self.programming = programming
        self.talent_platform = talent_platform
    
    def generate_income(self):
        # Code to generate income through collaborations, aggregators and accelerators investments
        pass
    
    def showcase_heritage(self):
        # Code to showcase the vibrance of India's heritage
        pass
    
    def attract_emerging_talent(self):
        # Code to provide a platform for emerging talent
        pass
    
    def bring_communities_together(self):
        # Code to bring together communities through programming of epic theatricals, regional theatre, music, dance, spoken word, etc.
        pass




destination = CulturalDestination("Mumbai", True, True, True, True)

@app.route('/destination', methods=['GET'])
def get_destination():
    destination_dict = {
        'city': destination.city,
        'visual_art_space': destination.visual_art_space,
        'public_art': destination.public_art,
        'programming': destination.programming,
        'talent_platform': destination.talent_platform
    }
    return jsonify(destination_dict)


    



class CulturalDestinationTest(unittest.TestCase):
    def setUp(self):
        self.destination = CulturalDestination("Mumbai", True, True, True, True)
    
    def test_city(self):
        self.assertEqual(self.destination.city, "Mumbai")
    
    def test_visual_art_space(self):
        self.assertTrue(self.destination.visual_art_space)
    
    def test_public_art(self):
        self.assertTrue(self.destination.public_art)
    
    def test_programming(self):
        self.assertTrue(self.destination.programming)
    
    def test_talent_platform(self):
        self.assertTrue(self.destination.talent_platform)

if __name__ == '__main__':
    unittest.main()
    app.run(debug=True)

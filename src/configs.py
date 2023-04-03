characters = [
    'Baby Peach, Baby Daisy',
    'Baby Rosalina, Lemmy',
    'Baby Mario, Baby Luigi, Dry Bones, Mii (Light)',
    'Toadette, Wendy, Isabelle',
    'Koopa Troopa, Lakitu, Browser Jr',
    'Toad, Shy Guy, Larry',
    'Cat Peach, Villager Female, Inkling Female',
    'Peach, Daisy, Yoshi',
    'Tanooki Mario, Villager Male, Inkling Male',
    'Mario, Ludwig, Mii (Medium)',
    'Luigi, Iggy',
    'Metal Mario, Pink Gold Peach, Gold Mario',
    'Rosalina, Link, King Boo',
    'Donkey Kong, Waluigi, Roy',
    'Wario, Dry Bowser',
    'Bowser, Morton, Mii (Heavy)'
]

karts = [
    'Standard Kart, The Duke',
    '300 SL Roadster',
    'Pipe Frame',
    'Varmint, City Tripper',
    'Mach 8, Sports Coupe',
    'Inkstriker',
    'Steel Driver, Tri-Speeder',
    'Bone Rattler',
    'Cat Cruiser, Teddy Buggy',
    'Comet, Yoshi Bike',
    'Circuit Special, B Dasher, P-Wing',
    'Badwagon, GLA',
    'Standard ATV (Quad)',
    'Prancer',
    'Sport Bike, Jet Bike',
    'Biddybuggy (Buggybud), Mr. Scooty',
    'Landship',
    'Streetle',
    'Sneeker',
    'Gold Standard (Gold Kart)',
    'Master Cycle',
    'Standard Bike, Flame Rider',
    'Wild Wiggler',
    'W 25 Silver Arrow',
    'Blue Falcon',
    'Splat Buggy',
    'Tanooki Kart',
    'Koopa Clown, Master Cycle Zero'
]

tires = [
    'Standard, Blue Standard',
    'GLA Tires',
    'Monster, Hot Monster',
    'Ancient',
    'Roller, Azure Roller',
    'Slim, Wood, Crimson Slim',
    'Slick, Cyber Slick',
    'Metal',
    'Gold Tires',
    'Button, Leaf Tires',
    'Off-Road, Retro Off-Road',
    'Triforce Tires',
    'Sponge',
    'Cushion'
]

gliders = [
    'Super Glider, Waddle Wing, Hylian Kite',
    'Cloud Glider, Parachute, Flower Glider, Paper Glider',
    'Wario Wing, Plane Glider, Gold Glider, Paraglider',
    'Peach Parasol, Parafoil, Bowser Kite, MKTV Parafoil'
]


def get_config(row):
    return {
        'character': characters[row['character'] - 1],
        'kart': karts[row['body'] - 1],
        'tire': tires[row['tire'] - 1],
        'glider': gliders[row['glider'] - 1]
    }

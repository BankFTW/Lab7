

mammals = [
    "Zebra",
    "Yak",
    "Wombat",
    "Wolverine",
    "Wolf",
    "Whale",
    "Weasel",
    "Water buffalo",
    "Walrus",
    "Wallaby",
    "Vicuna",
    "Tiger",
    "Tarsier",
    "Tapir",
    "Squirrel",
    "Skunk",
    "Shrew",
    "Sheep",
    "Seal",
    "Sea lion",
    "Rhinoceros",
    "Reindeer (caribou)",
    "Red panda",
    "Red deer",
    "Rat",
    "Ram",
    "Raccoon",
    "Rabbit",
    "Prairie Dog",
    "Porpoise",
    "Porcupine",
    "Pony",
    "Pig",
    "Panther",
    "Ox",
    "Otter",
    "Oryx",
    "Opossum",
    "Okapi",
    "Narwhal",
    "Mule",
    "Mouse",
    "Moose",
    "Monkey",
    "Mole",
    "Mink",
    "Meerkat",
    "Marten",
    "Manatee",
    "Loris",
    "Llama",
    "Lion",
    "Leopard",
    "Lemur",
    "Kudu",
    "Kouprey",
    "Koala",
    "Kangaroo",
    "Jaguar",
    "Jackal",
    "Hyena",
    "Human",
    "Horse",
    "Hippopotamus",
    "Hedgehog",
    "Hare",
    "Hamster"
]
birds = [
    "Wren",
    "Woodpecker",
    "Woodcock",
    "Vulture",
    "Turkey",
    "Swan",
    "Swallow",
    "Stork",
    "Starling",
    "Sandpiper",
    "Ruff",
    "Rook",
    "Raven",
    "Rail",
    "Quelea",
    "Quail",
    "Pigeon",
    "Pheasant",
    "Penguin",
    "Pelican",
    "Peafowl",
    "Partridge",
    "Parrot",
    "Owl",
    "Ostrich",
    "Nightingale",
    "Mallard",
    "Magpie",
    "Lyrebird",
    "Lark",
    "Lapwing",
    "Jay, Blue",
    "Jay",
    "Hummingbird",
    "Heron",
    "Hawk"
]
fish = [
    "Trout",
    "Stingray",
    "Shark",
    "Seahorse",
    "Sardine",
    "Salmon",
    "Herring"
]
reptiles = [
    "Viper",
    "Turtle",
    "Snake",
    "Komodo dragon",
]
amphibians = [
    "Toad",
    "Salamander",
    "Newt",
]
insect = [
    "Wasp",
    "Termite",
    "Stinkbug",
    "Mosquito",
    "Louse",
    "Locust",
    "Hornet",
]

mammals.reverse()
birds.reverse()
fish.reverse()
reptiles.reverse()
amphibians.reverse()
insect.reverse()

print("Mammals:")
for animal in mammals:
    print(animal)

print("Birds:")
for animal in birds:
    print(animal)

print("Fish:")
for animal in fish:
    print(animal)

print("Mammals:")
for animal in reptiles:
    print(animal)

print("Amphibians:")
for animal in amphibians:
    print(animal)

print("Insect:")
for animal in insect:
    print(animal)

f = open("animals-eng.txt", "r")
for line in f:
    if (line.strip() not in mammals and line.strip() not in birds and line.strip() not in fish
    and line.strip() not in reptiles and line.strip() not in amphibians and line.strip() not in insect):
        print(line.strip(), "does not exist")
f.close()
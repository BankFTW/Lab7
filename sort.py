

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

# print("Mammals:")
# for animal in mammals:
#     print(animal)

# print("Birds:")
# for animal in birds:
#     print(animal)

# print("Fish:")
# for animal in fish:
#     print(animal)

# print("Mammals:")
# for animal in reptiles:
#     print(animal)

# print("Amphibians:")
# for animal in amphibians:
#     print(animal)

# print("Insect:")
# for animal in insect:
#     print(animal)

# f = open("animals-eng.txt", "r")
# for line in f:
#     if (line.strip() not in mammals and line.strip() not in birds and line.strip() not in fish
#     and line.strip() not in reptiles and line.strip() not in amphibians and line.strip() not in insect):
#         print(line.strip(), "does not exist")
# f.close()

lst = [
    "Aardvark (mam)",
    "Albatross (Bird)",
    "Alligator (Reptiles)",
    "Alpaca (mam)",
    "Ant (insects)",
    "Anteater (mam) ",
    "Antelope (mam)",
    "Ape (mam)",
    "Armadillo (mam)",
    "Ass/Donkey (mam)",
    "Baboon (mam)",
    "Badger (mam)",
    "Barracuda (Fish)",
    "Bat (mam)",
    "Bear (mam)",
    "Beaver (mam)",
    "Bee (insects)",
    "Bison (mam)",
    "Boar (mam)",
    "Buffalo, African (mam)",
    "Galago (Others)",
    "Butterfly (insects)",
    "Camel (mam)",
    "Caribou (mam)",
    "Cat (mam)",
    "Caterpillar (insects)",
    "Cattle (mam)",
    "Chamois (mam)",
    "Cheetah (mam)",
    "Chicken (bird)",
    "Chimpanzee (mam)",
    "Chinchilla (mam)",
    "Chough (bird)",
    "Clam (Others)",
    "Cobra (reptile)",
    "Cockroach (insects)",
    "Cod (fish)",
    "Cormorant (bird)",
    "Coyote (mam)",
    "Crab (Other)",
    "Crane (Bird)",
    "Crocodile (reptile)",
    "Crow (bird)",
    "Curlew (bird)",
    "Deer (mam)",
    "Dinosaur (Other)",
    "Dog (mam)",
    "Dogfish (fish)",
    "Dolphin (mam)",
    "Donkey (mam)",
    "Dotterel (bird)",
    "Dove (bird)",
    "Dragonfly (insect)",
    "Duck (bird)",
    "Dugong (mam)",
    "Dunlin (bird)",
    "Eagle (bird)",
    "Echidna (mam)",
    "Eel (fish)",
    "Eland (mam)",
    "Elephant (mam)",
    "Elephant seal (mam)",
    "Elk (wapiti) (mam)",
    "Emu (bird)",
    "Falcon (bird)",
    "Ferret (mam)",
    "Finch (bird)",
    "Fish (mam)",
    "Flamingo (bird)",
    "Fly (insects)",
    "Fox (mam)",
    "Frog (amphi)",
    "Gaur (mam)",
    "Gazelle (mam)",
    "Gerbil (mam)",
    "Giant Panda (mam)",
    "Giraffe (mam)",
    "Gnat (insect)",
    "Gnu (mam)",
    "Goat (mam)",
    "Goose (bird)",
    "Goldfinch (bird)",
    "Goldfish (fish)",
    "Gorilla (mam)",
    "Goshawk (bird)",
    "Grasshopper (insects)",
    "Grouse (bird)",
    "Guanaco (mam)",
    "Guinea fowl (bird)",
    "Guinea pig (mam)",
    "Gull (bird)"
]

types = ["mam", "bird", "fish", "amphi", "reptile", "insects"]

for t in types:
    print(t)
    for anim in lst:
        new = anim.lower()
        if t in new:
            length = len(t) + 3
            print(anim[:-length])
    print()

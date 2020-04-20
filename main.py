from animals import EarthWorms, Terrapins, Rattlesnake, Mice, Ant, Finch, BettaFish, CopperHead, Gerbil, Parakeet
from habitats import IAquarium, ICage, IDirt, IGrassy, IAmazon



earthworm = EarthWorms("WormDude")
terrapin = Terrapins("Terrible")
snake = Rattlesnake("Rattle")
mouse = Mice("MouseBro")
ant = Ant("AntBro")
finch  = Finch("FinchBro")
betta = BettaFish("BettaBro")
copperhead = CopperHead("CopperNotBronze")
gerbil = Gerbil("Gerbs")
skeet = Parakeet("SKEET")

cage = ICage("The Bird Trap")
land_container = IGrassy("Land Walkers")
underworld = IDirt("Diggers")
aquarium = IAquarium("ShamooIsNumberOne")
amazon = IAmazon("Slitheren")


cage.add_animal(finch, skeet)
land_container.add_animal(ant, mouse)
underworld.add_animal(earthworm, ant, mouse, gerbil)
aquarium.add_animal(betta)
amazon.add_animal(copperhead, snake)

print(earthworm)
print(terrapin)
print(snake)
print(mouse)
print(ant)
print(finch)
print(betta)
print(copperhead)
print(gerbil)
print(skeet)

print(cage, land_container, underworld, aquarium, amazon)

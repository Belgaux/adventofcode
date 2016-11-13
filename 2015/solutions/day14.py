class Reindeer(object):
    def __init__(self, name, speed, max_fuel, rest_duration):
        self.name = name
        self.speed = speed # in km/s
        self.max_fuel = max_fuel # in seconds
        self.fuel = self.max_fuel
        self.rest_duration = rest_duration # in seconds
        self.rested_amount = 0
        self.distance_travelled = 0
        
    def tick(self):
        if self.fuel > 0:
            self.fuel -= 1
            self.distance_travelled += self.speed
        else:
            self.rest()
          
    def rest(self):
        if self.rested_amount == self.rest_duration:
            self.rested_amount = 0
            self.fuel = self.max_fuel
            self.tick()
        else:
            self.rested_amount += 1
                
def simulate_race(reindeer, length=1000):
    def get_leader():
        leader = [reindeer[0]]
        for r in reindeer:
            if r.distance_travelled > leader[0].distance_travelled:
                leader = [r]
            elif r.distance_travelled == leader[0].distance_travelled:
                leader.append(r)
        return leader
                
    leaderboard = {}
    for r in reindeer:
        leaderboard[r] = 0
    
    for _ in range(length):
        for r in reindeer:
            r.tick()
        leader = get_leader()
        for l in leader:
            leaderboard[l] += 1
        
    #winner = max(reindeer_list, key=lambda x: x.distance_travelled)    
    #print("Winner is {} with {} km travelled.".format(winner.name, winner.distance_travelled))

    winner = max(leaderboard, key=lambda x: leaderboard[x])    
    print("Winner is {} with {} points.".format(winner.name, leaderboard[winner]))
            
def main():
    text = [line.split() for line in open("../inputs/input14.txt").readlines()]
    reindeer = [Reindeer(line[0], int(line[3]), int(line[6]), int(line[-2])) for line in text]
    simulate_race(reindeer, 2503)
    
    
if __name__ == "__main__":
    main()
    
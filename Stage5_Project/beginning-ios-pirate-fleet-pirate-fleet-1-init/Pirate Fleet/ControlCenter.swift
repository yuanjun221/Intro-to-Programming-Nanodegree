//
//  ControlCenter.swift
//  Pirate Fleet
//
//  Created by Jarrod Parkes on 9/2/15.
//  Copyright © 2015 Udacity. All rights reserved.
//

struct GridLocation {
    let x: Int
    let y: Int
}

struct Ship {
    let length: Int
    let location: GridLocation
    let isVertical: Bool
}

struct Mine: _Mine_ {
    let location: GridLocation
    let explosionText: String
}

class ControlCenter {
    
    func addShipsAndMines(human: Human) {
        let smallShip = Ship(length: 2, location: GridLocation(x: 0, y: 0), isVertical: false)
        let mediumShip1 = Ship(length: 3, location: GridLocation(x: 4, y: 0), isVertical: false)
        let mediumShip2 = Ship(length: 3, location: GridLocation(x: 0, y: 1), isVertical: true)
        let largeShip = Ship(length: 4, location: GridLocation(x: 3, y: 1), isVertical: true)
        let extraLargeShip = Ship(length: 5, location: GridLocation(x: 2, y: 7), isVertical: false)
        
        human.addShipToGrid(smallShip)
        human.addShipToGrid(mediumShip1)
        human.addShipToGrid(mediumShip2)
        human.addShipToGrid(largeShip)
        human.addShipToGrid(extraLargeShip)
        
        let message = "You've hit a mine!"
        
        let mine1 = Mine(location: GridLocation(x: 5, y: 5), explosionText: message)
        let mine2 = Mine(location: GridLocation(x: 5, y: 4), explosionText: message)
        
        human.addMineToGrid(mine1)
        human.addMineToGrid(mine2)
    }
    
    func calculateFinalScore(gameStats: GameStats) -> Int {
        
        var finalScore: Int
        
        let enemyShipsSunk = 5 - gameStats.enemyShipsRemaining
        let sinkBonus = gameStats.sinkBonus
        let humanShipsRemaining = 5 - gameStats.humanShipsSunk
        let shipBonus = gameStats.shipBonus
        let numberOfGuesses = gameStats.numberOfHitsOnEnemy + gameStats.numberOfMissesByHuman
        let guessPenalty = gameStats.guessPenalty
        
        finalScore = enemyShipsSunk * sinkBonus + humanShipsRemaining * shipBonus - numberOfGuesses * guessPenalty
        
        return finalScore
    }
}
//console.log(count)
//https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics
//https://www.youtube.com/watch?v=jS4aFq5-91M  (44:30)
//https://www.youtube.com/watch?v=5IMXpp3rohQ (34:20)

const canvas = document.querySelector("canvas")
const c = canvas.getContext("2d")
canvas.width = innerWidth
canvas.height = innerHeight

class Boundary {
    constructor({position}){
        this.position = position
        this.width = 50
        this.height = 50
    }

    draw(){
        c.fillStyle = "white"
        c.fillRect(this.position.x, this.position.y, this.width, this.height)
    }
}

const map = [
    ["-","-","-","-","-","-","-","-","-","-","-","-","-"],
    ["-"," "," "," "," "," "," "," "," "," "," "," ","-"],
    ["-","-","-"," ","-"," ","-"," ","-"," ","-","-","-"],
    ["-","-","-"," ","-"," ","-"," ","-"," ","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-","-","-","-"]
]

const boundaries = []


map.forEach((row, yIn) =>{
    row.forEach((symbol, xIn) =>{
        switch (symbol) {
            case "-":
                boundaries.push(
                    new Boundary({
                        position:{
                            x:50 * xIn,
                            y:50 * yIn
                        }
                    })
                )
                break
        }
    })
})

boundaries.forEach((boundary) => {
    boundary.draw()
})

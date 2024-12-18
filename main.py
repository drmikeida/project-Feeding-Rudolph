import pyxel


class App:

    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)

        pyxel.load("my_resource.pyxres")

        # Set the initial position of the square
        self.x = 75
        self.y = 55
        self.score = 0
        self.dx = 2
        self.dy = 2

        # Set the initial position and velocity of the sprite
        self.sprite_x = 80
        self.sprite_y = 60
        self.sprite_dx = 2
        self.sprite_dy = 2

        # Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.dy
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.dy
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.dx
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.dx

        # Simple interaction: Increase score when square touches circle
        if self.x <= self.sprite_x + 1 and self.x >= self.y - 2 and self.y <= self.sprite_y + 1 and self.y >= self.sprite_y - 2:
            self.score += 1            

        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy

        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 160:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1

        if self.x <= 0:
            self.x = 0
        if self.x >= 160:
            self.x = 149
        if self.y <= 0:
            self.y = 0
        if self.y >= 120:
            self.y = 109
            

    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(0)

        # Draw a square (color 9)
        #pyxel.rect(self.x, self.y, 10, 10, 9)

        #tile map
        pyxel.bltm(1, 1, 0, 0, 0, 160, 120)

        # Draw the moving sprite (color 11)
        #pyxel.circ(self.sprite_x, self.sprite_y, 5, 11)

        pyxel.blt(self.sprite_x, self.sprite_y, 0, 16, 0, 16, 16, 1)

        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)

        #Display reindeer
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 0)

        # Display a message when score is high
        if self.score >= 5:
            pyxel.text(50, 50, "You're cooking!", 12)


# Run the game
App()

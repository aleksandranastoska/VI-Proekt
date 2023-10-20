import othello

def main():
    game = othello.Othello()
    game.draw_board()
    game.initialize_board()
    game.time_limit = 5

    game.run()


main()
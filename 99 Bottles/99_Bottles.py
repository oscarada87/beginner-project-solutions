def check_lyrics(n):
    if n == 0:
        no_bottle_lyrics = """No more bottles of beer on the wall, no more bottles of beer.\n 
Go to the store and buy some more, 99 bottles of beer on the wall."""
        return no_bottle_lyrics
    elif n == 1:
        one_bottle_lyrics = """1 bottle of beer on the wall, 1 bottle of beer.\n
Take one down and pass it around, no more bottles of beer on the wall."""
        return one_bottle_lyrics
    else:
        bottles_lyrics = """{} bottles of beer on the wall, {} bottles of beer.\n
Take one down and pass it around, {} bottle of beer on the wall.""".format(str(n), str(n), str(n-1))
        return bottles_lyrics

def print_lyrics():
    for n in range(99, -1, -1):
        print(check_lyrics(n)) 

def main():
    print_lyrics()

if __name__ == "__main__":
    main()
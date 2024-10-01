liked_post = []

while True:
    liking = input("Like post? (Y/N): ")

    if liking == "Y":
        user_name = input("Your name: ")
        liked_post.append(user_name)

        if len(liked_post) == 2:
            print("{} and {} like this post.".format(liked_post[0], liked_post[1]))
        elif len(liked_post) == 3:
            print("{}, {} and {} like this post.".format(liked_post[0], liked_post[1], liked_post[2]))
        elif len(liked_post) > 3:
            print("{} and {} others like this post.".format(liked_post[0], len(liked_post) - 1))
    else:
        break

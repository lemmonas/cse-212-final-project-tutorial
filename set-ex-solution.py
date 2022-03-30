signed_up = set()
def single_sign_up(name):
    length = len(signed_up)
    signed_up.add(name)
    if length == len(signed_up):
        print("Sorry! You've already signed up")
    else:
        print("Sign up successful!")

single_sign_up("Bob")
single_sign_up("Sue")
single_sign_up("Sue")
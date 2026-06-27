from pyscript import web, when #type: ignore
from random import randint
import js # type: ignore

# Hide the loading screen once Pyscript is loaded
Loading_Screen = web.page["#Loading_Screen"]
Loading_Screen.style["display"] = "none"

Num = randint(1, 10)
Attempts = 1

User_Num = web.page["#user_num"]
Guess_Button = web.page["#guess_button"]
Output = web.page["#output"]

@when ("click", Guess_Button)
def Guess():
    User_Num_Value = User_Num.value.strip()
    Input_Conditions = [str(User_Num_Value) == '', not User_Num_Value.isdigit()]

    if any(Input_Conditions):
        Output.innerHTML = "Enter a valid integer!"
        return
    elif int(User_Num_Value) < 1 or int(User_Num_Value) > 10:
        Output.innerHTML = "The number is between 1 and 10."
        return
    
    User_Num_Value = int(User_Num_Value)
    
    if User_Num_Value != Num:
        Output.innerHTML = "Wrong! Try again."
        global Attempts
        Attempts += 1
    elif User_Num_Value == Num:
        Output.innerHTML = f"Well done! You guessed my number ({Num}) in {Attempts} attempts."
        Play_Again_Text = web.p("Would you like to play again? (This reloads the page)")
        Play_Again_Button = web.button("Play Again")
        web.page.body.append(Play_Again_Text, Play_Again_Button)
        @when ("click", Play_Again_Button)
        def Play_Again():
            js.window.location.reload()
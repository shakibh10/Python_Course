from colorama import Fore, Style, init
from pyfiglet import Figlet
import time
import os

# Initialize colorama
init()

# Function to display a sad face
def print_sad_face():
    sad_face = [
        "        *****        *****        ",
        "      *********    *********      ",
        "    ***************************   ",
        "   *****************************  ",
        "  ******************************* ",
        "   *****************************  ",
        "    ******               ******   ",
        "     ****   :(       :(   ****    ",
        "      **                   **     ",
        "       **               **        ",
        "        *****************         ",
        "          *************           ",
        "            *********             ",
        "              *****               ",
        "                *                 ",
    ]

    for line in sad_face:
        print(Fore.BLUE + line.center(80))
        time.sleep(0.1)
    print(Style.RESET_ALL)

# Function to display the message in an artistic font and color
def print_message():
    fig = Figlet(font='slant')
    message = "I Miss You, Jui"
    styled_message = Fore.CYAN + Style.BRIGHT + fig.renderText(message)
    print(styled_message)
    print(Style.RESET_ALL)

# Function to add sad effects
def sad_effect():
    tears = ["😢", "😭", "💔", "😞", "😔"]
    for _ in range(10):
        print(" ".join(Fore.LIGHTBLUE_EX + tears[_ % len(tears)] for _ in range(30)).center(80))
        time.sleep(0.2)
    print(Style.RESET_ALL)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    sad_effect()
    print_sad_face()
    time.sleep(0.5)
    print_message()
    sad_effect()


# #<div className=" m-24">


#         <div className="">

#         <div className=" flex items-center justify-center "><p className="rounded-lg text-violet-400 bg-orange-100 text-center w-fit" >Getuigenissen</p></div>
#     <h1  className="text-4xl text-center font-bold">Wat klanten over ons zeggen</h1>
    
#         </div>



#         <div className=" flex gap-10 ml-44 mr-44 mt-6 items-center">

#         <div className="card bg-base-100 w-72 shadow-xl h-80">
#                         <div className="card-body">
#                         <div className="flex justify-between items-center gap-6">
#                             <div className=""><img src="/avatar/avater-testi-1.png.png" alt="" /></div>
#                             <div className="">
#                                 <div className="text-base"><p>Lisa van Dijk</p></div>
#                                  <div className="text-xs text-slate-400 "><p>eigenaar van een retailbedrijf</p></div>
#                             </div>
#                         </div>
#                             <p className="text-xs mt-10 text-left">“Dankzij Younitech hebben we een enorme toename gezien in
#                                  onze online zichtbaarheid en klantbetrokkenheid. Hun team is creatief en resultaatgericht.”</p>
#                             <div className="card-actions justify-end">
#                             </div> 
#                         </div>
#                  </div>  






#                  <div className="card bg-base-100 w-72 shadow-xl h-80">
#                         <div className="card-body">
#                         <div className="flex justify-between items-center gap-6">
#                             <div className=""><img src="/avatar/avater-testi-2.png.png " alt="" /></div>
#                             <div className="">
#                                 <div className="text-base"><p>Tom Jansen</p></div>
#                                  <div className="text-xs text-slate-400"><p>marketingmanager bij een </p></div>
#                             </div>
#                         </div>
#                             <p className="text-xs mt-10 text-left">“De campagnes van Younitech hebben niet alleen onze conversies 
#                                 verdubbeld, maar ook onze merkbekendheid aanzienlijk vergroot.”</p>
#                             <div className="card-actions justify-end">
#                             </div> 
#                         </div>
#                  </div>  



                        
#      </div>
# </div>

        


















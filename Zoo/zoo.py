print("I love animals!")
print("Let`s check out the animails ...")
print("The deer looks fine")
print("The lion looks healthy.")
#------------------------------------------
#2-st Stage
#print("If you want see a camel - input \"camel\"")
#zoo = input("input choice > ")

#print("You input - " + zoo)
#camel=r"""The camel habitat...
#        ___.-''''-.
#     /___  @    |
#      ',,,,.     |         _.'''''''._
#           '     |        /           \
#           |     \    _.-'             \
#           |      '.-'                  '-.
#           |                               ',
#           |                                '',
#            ',,-,                           ':;
#                 ',,| ;,,                 ,' ;;
#                    ! ; !'',,,',',,,,'!  ;   ;:
#                   : ;  ! !       ! ! ; ;   ;,
#                   ; ;   ! !      ! !  ; ;   ; ;
#                  ; ;    ! !     ! !   ; ;
#                  ; ;    ! !    ! !    ; ;
#                 ;,,      !,!   !,!     ;,;
#                 /_I      L_I   L_I     /_I
#
#Look at that!"""
#if zoo == "camel":
#    print (camel)
#------------------------
#3-st Stage
#-----------------------
#4-st Stage
print ("Animal list: 1-camel, 2-rabbit, 3-deer, 4-goose, 5-bat")

animals = [r"""
The camel habitat...
        ___.-''''-.
     /___  @    |
      ',,,,.     |         _.'''''''._
           '     |        /           \
           |     \    _.-'             \
           |      '.-'                  '-.
           |                               ',
           |                                '',
            ',,-,                           ':;
                 ',,| ;,,                 ,' ;;
                    ! ; !'',,,',',,,,'!  ;   ;:
                   : ;  ! !       ! ! ; ;   ;,
                   ; ;   ! !      ! !  ; ;   ; ;
                  ; ;    ! !     ! !   ; ;
                  ; ;    ! !    ! !    ; ;
                 ;,,      !,!   !,!     ;,;
                 /_I      L_I   L_I     /_I

Look at that!""",
r"""
       /|      __
      / |   ,-~ /
     Y :|  //  /
     | jj /( .^
     >-"~"-v"
        / Y
       jo o |
      ( ~T~ j
       >._-' _.
      /       "~"|
     Y         _, |
    /|   ;-"~ _ l
   / l/ ,-"~    \
  \//\/      .-  \
      Y      /    Y
      l      I     !
      ]\ _\  /"\  
     (" ~----( ~   Y. )
     
It looks fine!
---
You've reached the end of the program.

""",r"""
     /|       |\
` __\\       //__'
      ||      ||
  \__`\     |'__/
     `_\\   //_'
     _ ,:---;, _
      \_:    :_/
        |@  @|
        |    |
       ,\ -- / \
        ;;`-'   `---__________---------------- 
         ;;;                                  \_\
         ';;;                                  |
          ;    |                              ;
          \   \       \        |            /
            \_, \     /        \         |\
               |';|   |,,,,,,,,/ \       \ \_
               |   |   |           \     /    |
                \   \   |           |   / \   |
                |  ||  |           |  |   |  |
                |  ||  |           |  |   |  |
                |  ||  |           |  |   |  |
                |_| |_|            |_|    |_|
               /_/ /_/            /_/     /_/

""",
r"""
                           _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
""",
r"""
           _______________               _________________
 ~-.              \  |\___/|  /              .-~
     `-.           \ / o o \ /           .-'
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
"""]

choice = ""
while choice != "exit":
    choice = input("Please enter the number of the habitat or 'exit' to quit: ")

    if choice.isdigit() and 0 <= int(choice) <=5:
        index=int(choice)-1
        print(animals[index])

    elif choice != "exit":
        print("Invalid input! Please enter a valid number between 0 and 5 or 'exit'.")

print("See you later!")

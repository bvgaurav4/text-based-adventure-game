from tkinter import *
from tkinter.scrolledtext import ScrolledText
gg = Tk()
gg.title("Text Based Adverture game")
d=Button(gg,text="start",fg="orange",bg="purple",font="bold")
def start():
 d.destroy()   
 f = Frame(gg)
 st = ScrolledText(f, width=100, height=50)
 st.pack(fill=BOTH, side=LEFT, expand=True)
 f.pack()
 st.insert(END,"WELCOME TO TEXT BASED ADVENTURE GAME")
 st.insert(END,"You are lancelot and the town people call you engineering god because of your"
          " ingenious inventions.\nU made ur fortune by ur inventions")
 st.insert(END,"\nOne day u wake up and see that all ur fortune has been stolen from ur safe , and there is no sign of ur wife.\n u search the whole house for clues but wont find any")
 st.insert(END,"What do you want to do?")
 def s1():
    c1 = Checkbutton(f, text=" 1)go to the post office")
    c1.pack()
    c2 = Checkbutton(f, text="2)go to the bar")
    c2.pack()
    def buttonhdl1():
        c2.deselect()
        st.insert("   There are no letters for you")
    def buttonhdl2():
        c1.deselect()
        st.insert(END,"""  IN THE BAR  :
                                baxter: hey mate how r u?, I heard that u were robbed .
                                you: ahhh yea those thugs took all my fortune without
                                leaving a single clue (sigh).
                                baxter: hmm what if some one u close to u did it cause
                                no one knows how ur inventions work.
                                you: hmm u have a good point.""")                      
        def s2():
            st.insert(END,"What do you want to do?")
            c3 = Checkbutton(f,text="1)hang around looking for more info")
            c3.pack()
            c4 = Checkbutton(f,text="2)leave the bar")
            c4.pack()
            def buttonhdl1():
                c4.deselect()
                st.insert(END,"no extra information available in the bar")
            def buttonhdl2():
                c3.deselect()
                st.insert(END," \nokay you are outside the bar.\n What do you want to do \n")
                c5 = Checkbutton(f, text="1)to the village headman\n")
                c6 = Checkbutton(f, text="2)home")
                c5.pack()
                c6.pack()
                def buttonhdl1():
                    c6.deselect()
                    st.insert(END,"   you lodge a complaint about the robbery and the headman promises to do as muc as he can.")
                def buttonhdl2():
                    c5.deselect()
                    st.insert(END,"    AT HOME \nWhat do you want to do?\n")
                    def s3():
                        c7 = Checkbutton(f, text=")check the bulding windows for damage")
                        c8 = Checkbutton(f, text="2).check the safe for damages")
                        c9 = Checkbutton(f, text="3).check the garden.")
                        c7.pack()
                        c8.pack()
                        c9.pack()
                        def buttonhdl1():
                            c8.deselect()
                            c9.deselect()
                            st.insert(END,"  \n hmm the bulding windoes r not damaged ")
                        def buttonhdl2():
                            c7.deselect()
                            c9.deselect()
                            st.insert(END,"\nwait the safe is also not damaged \n hmmm now i have a feeling that someone who knows about my inventions stole my fortune")
                        def buttonhdl3():
                            c7.deselect()
                            c8.deselect()
                            st.insert(END,"\n hmm cart trails hmm i guess they used a cart to steal my fortune")
                            def s4():
                                c10 = Checkbutton(f, text="1).follow the  trail")
                                c11 = Checkbutton(f, text="2).look around to find more clues")
                                c10.pack()
                                c11.pack()
                                def buttonhdl4():
                                    c11.deselect()
                                    st.insert(END,"hmm a clearing and there is a cart ")
                                    def  l():
                                        st.insert(END,"want to check the cart?(y/n)")
                                        l1 = Checkbutton(f, text="y")
                                        l1.pack()
                                        l2 = Checkbutton(f, text="n")
                                        l2.pack()
                                        def buttonhdl1():
                                            l2.deselect()
                                            st.insert(END," hmm this cart is not designed by me \n let me check inside \n oh there is a letter \t\t\t  LETTER\nahhh lancelot i am the one who stole ur fortune .\nU and your arogant behaviour was making me sick it serves u right ")
                                            s4()
                                        def buttonhdl2():
                                            l1.deselect()
                                            s4()
                                        l1.configure(command=buttonhdl1)
                                        l2.configure(command=buttonhdl2)
                                    l()
                                def buttonhdl2():
                                    c10.deselect()
                                    st.insert(END,"   hmm let me look around \n wait is that gold.... \n there is a trail of gold here!!....  ")
                                    st.insert(END,"   \n FOLLOWING THE GOLD COIN TRAIL\nhmm the apparatus, its a living thing which uses pure metal as blood ./n It looks down for some reason and its following me from the start of the trail i wonder why\n well i have to find the one who took my  fortune \n   CONTINUES TO FOLLOW THE TRAIL\nyou:AHHH i found my fortune\nyou: whaat.. r u doing here emma\nEmma:hi lancelot i was the one who took ur fortune \n you: that explains y the safe was not damaged \n Emma : you were so  polite and kind when u were inventing but now u have become arrogant and rude  because of ur fortune\n.U r not the lancelot that i knew\nyou : so v r on our ways now \n Emma: i will be waiting\nyou: hmm i offered my to people who needed it but they refused it now what will i do with this money \nThe apparatuse maintains the land there is no doubt that there is spikes every where \nmaybe i will give the gold to the appratus and save its life")
                                    def s7():
                                        st.insert(END,"\n \n would u like to save the apparatus ")
                                        ic = Checkbutton(f, text="y")
                                        ic1 = Checkbutton(f, text="y")
                                        ic.pack()
                                        ic1.pack()
                                        def b():
                                            ic1.deselect()
                                            st.insert(END,"\nthe apparatus (-_-)->(>_<)->(*,*) ")
                                        def b2():
                                            ic.deselect()
                                            st.insert(END,"\n the apparatus (-_-)->(>_<)->(*,*) ")
                                        ic.configure(command=b)
                                        ic1.configure(command=b2)
                                    s7()    
                                c10.configure(command=buttonhdl4)
                                c11.configure(command=buttonhdl2)
                            s4()
                        c7.configure(command=buttonhdl1)
                        c8.configure(command=buttonhdl2)
                        c9.configure(command=buttonhdl3)
                    s3()
                c5.configure(command=buttonhdl1)
                c6.configure(command=buttonhdl2)
            c3.configure(command=buttonhdl1)
            c4.configure(command=buttonhdl2)
        s2()
    c1.configure(command=buttonhdl1)
    c2.configure(command=buttonhdl2)
 s1()   
 def a(x):
    x()
 a(start)
d.configure(command=start)
d.pack()
gg.mainloop()
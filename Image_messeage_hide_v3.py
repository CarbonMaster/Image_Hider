from PIL import Image, ImageDraw
import numpy as np
import hashlib
import tkinter as tk

#root = tk.Tk()
#root.title("Moja aplikacja")

#button = tk.Button(root, text="Kliknij mnie")
#button.pack()  # Dodaj przycisk do okna

#label = tk.Label(root, text="To jest etykieta")
#label.pack()

#entry = tk.Entry(root)
#entry.pack()

#checkbox = tk.Checkbutton(root, text="Zaznacz mnie")
#checkbox.pack()

def on_button_click():
    label.config(text="Naciśnięto przycisk")

#button = tk.Button(root, text="Kliknij mnie", command=on_button_click)

#hasher = hashlib.sha256()

#Główna pętla programu
def encode():
    #Inicjalizuje obrazy
    print("Encoding procedure.\nRemember, that smaller image will be encoded!")

    print("Input first image name and extention (ex. image1.png)")
    #img1_name = input()
    print("Input second image name and extention (ex. image2.png)")
    #img2_name = input()



    #jbdglavjdsvjcavksdbvl
    img1_name = "image1.png"
    img2_name = "image4.png"
    #jbdglavjdsvjcavksdbvl


    t_image1 = Image.open(img1_name)
    t_image2 = Image.open(img2_name)
    t_width1, t_height1 = t_image1.size
    t_width2, t_height2 = t_image2.size
    
    
    if t_width1 * t_height1 >= t_width2 * t_height2:
        #Obraz 2 jest wiadomoscia
        if t_width1>=t_width2 and t_height1>=t_height2:
            image2 = Image.open(img1_name)
            image1 = Image.open(img2_name)
            image3 = Image.open(img1_name)
        else:
            print("Images are not compatible to conversion due to size limits (uno)")
    elif t_width1 * t_height1 < t_width2 * t_height2:
        #Obraz 1 jest wiadomoscia
        if t_width2>=t_width1 and t_height2>=t_height1:
            image1 = Image.open(img1_name)
            image2 = Image.open(img2_name)
            image3 = Image.open(img2_name)
        else:
            print("Images are not suitable to conversion due to size limits (dos)")
            

    

    print("Do you want to show output image? (y/n)")
    show = False
    while True:
        anwser = input()
        if anwser == "y" or anwser == "Y":
            show_img = True
            break
        if anwser == "n" or anwser == "N":
            show_img = False
            break
        else:
            print("Incorrect anwser. Try again. Insert y for Yes or n for No.")

    print("Encoding...")

    

    image1 = image1.convert("RGBA")
    #image2 = image2.convert("RGB")
    image2 = image2.convert("RGBA")
    
    

    pixels1 = image1.load()
    pixels2 = image2.load()

    width_1, height_1 = image1.size
    for x in range(width_1):
        for y in range(height_1):
            r, g, b, a = pixels1[x, y]
            a = 255  # Ustaw kanał alfa na maksymalną wartość (255)
            pixels1[x, y] = (r, g, b, a)

    width_2, height_2 = image2.size
    for x in range(width_2):
        for y in range(height_2):
            r, g, b, a = pixels2[x, y]
            #a = 255  # Ustaw kanał alfa na maksymalną wartość (255)
            #pixels2[x, y] = (r, g, b, a)

    for x in range(width_1):
        for y in range(height_1):
            r, g, b, a = pixels1[x, y]
            r = round(r * (a / 255))
            g = round(g * (a / 255))
            b = round(b * (a / 255))
            pixels1[x, y] = (r, g, b, a)
    
    #image1.putalpha(255)
    
    
    
    
    image1 = image1.convert("L")
    #image2 = image2.convert("L")

    # Pobierz dane pikseli z obrazow
    pixels1 = list(image1.getdata())
    pixels2 = list(image2.getdata())

    # Porównaj rozmiary obrazów
    width1, height1 = image1.size
    width2, height2 = image2.size


    #Jezeli obraz 1 jest wiekszy lub taki sam, wtedy

    
    
    modified_pixels = [round(100 * pixel / 255) for pixel in pixels1]
    modified_image_temp = Image.new("RGBA", image1.size)
    modified_image_temp.putdata(modified_pixels)

    red_channel = modified_image_temp.split()[0]
    modified_image_temp.putalpha(red_channel)

    new_image = Image.new("RGBA", modified_image_temp.size, (0, 0, 0, 0))
    new_image.putalpha(modified_image_temp.split()[3])

    image2.putalpha(255)
    background = image2.convert("RGBA")

    white_background = Image.new("RGBA", image2.size)

    for y in range(white_background.height):
        for x in range(white_background.width):
            r_bg, g_bg, b_bg, a_bg = background.getpixel((x,y))
            white_background.putpixel((x,y),(r_bg, g_bg, b_bg, 255))
            
    white_background.show()        
    
    top_image = new_image.convert("RGBA")
    
    bg_width, bg_height = white_background.size

    result = Image.new("RGBA", (bg_width, bg_height))
    result.paste(white_background, (0, 0))
    
    paste_x = (bg_width - top_image.width) // 2
    paste_y = (bg_height - top_image.height) // 2
    
    #background = image3.convert("RGBA")

   # for y in range(white_background.height):
   #     for x in range(white_background.width):
   #         r_bg, g_bg, b_bg, a_bg = white_background.getpixel((x,y))
   #         if r_bg==0 and g_bg==0 and b_bg ==0:
            #    r_bg=255
            #    g_bg=255
            #    b_bg=255
            #    a_bg=255
            #white_background.putpixel((x,y),(r_bg, g_bg, b_bg, a_bg))
    
    for y in range(top_image.height):
        for x in range(top_image.width):
            r_bg, g_bg, b_bg, a_bg = white_background.getpixel((paste_x + x, paste_y + y))
            
            r_top, g_top, b_top, a_top = top_image.getpixel((x, y))
            new_alpha = a_bg - a_top

            # Ensure the alpha value is within the 0-255 range
            new_alpha = max(0, min(255, new_alpha))

            # Set the new pixel in the result image
            result.putpixel((paste_x + x, paste_y + y), (0, 0, 0, new_alpha))

    for y in range(background.height):
        for x in range(background.width):
            r_bg, g_bg, b_bg, a_bg = white_background.getpixel((x,y))
            if r_bg==0 and g_bg==0 and b_bg ==0:
                r_bg=255
                g_bg=255
                b_bg=255

            r_res, g_res, b_res, a_res = result.getpixel((x, y))

            result.putpixel((x,y), (r_bg, g_bg, b_bg, a_res))
            
    
    if show_img == True:
        result.show()

        
    print("Call your output file (without extention), or press CTRL + C to abort.")

    #result.save(input()+".png")
    result.save("encoded.png")
    
    return







#Tutaj dokonuje odzyskania obrazu z tego gowna
def decode():
    image_converted = Image.open("encoded.png")

    width_o, height_o = image_converted.size

    decoded_image = Image.new("RGBA", (width_o, height_o) )

    pixels = list(image_converted.getdata())

    min_alpha = 255 
    max_alpha = 255

    for pixel in pixels:
        temp = pixel[3]

        if temp < min_alpha and temp > 0:
            min_alpha = temp

    temp = max_alpha - min_alpha

    for x in range(width_o):
        for y in range(height_o):
            alpha_value = pixels[y * width_o + x][3]  # Odczytaj wartość alfa (A)
            
            #if alpha_value < 255:
            #    alpha_value = 255 - alpha_value
    
            #alpha_value = round(((alpha_value)/temp)*255)

            #if alpha_value < min_alpha:
            #    min_alpha = temp

            #alpha_value = int((alpha_value - min_alpha) / (max_alpha - min_alpha) * 255)
            #print(alpha_value)
            alpha_value = round(((255-alpha_value)/temp)*255)
            new_pixel = (alpha_value, alpha_value, alpha_value, 255)

            decoded_image.putpixel((x, y), new_pixel)

    #print(max_alpha)
    print(min_alpha)


    
    #decoded_image.show()
    decoded_image.save("decoded.png")
    return





def main():
    #root.mainloop()
    #try:
    #    print("Input desired operation number: ")
    #    Input = input()
    #    if (Input == "1"):
    #        encode()
     #   elif (Input == "2"):
    #        decode()
    encode()
    decode()
        
    #except:

    #    print("Program failed or aborted")
    #return



main()




#LEft to do:
#Interfejs graficzny
#Określanie które obrazy do konwersji
#Sprawdzanie obrazu do włożenia rozmiary i pętla uzupełnić
#Oddzielne funkcje do szyfrowania i dekodowania
#Dodatkowe utrudnienie w dostrzeżeniu szyfrowania poprzez dodanie wachań wartości kolorów
#Zmniejszanie obrazu wyjściowego ma bazie braku kolorów
#Dodać obraz który kodowany  jest z pomocą określonego seed-a (jego kolory) [szyfr kodujący i rozkodowujący do obrazu]
#Dodać funkcję image scramble
#Dodać kodowanie na background jako pusty obraz, rozmiarowo identyczny jak wiadomość

#Z obrazu background trzeba usuwać całą przezroczystość, dosłownie. lub nakladac same wartosci rgb na obraz bialy


import turtle, random, time #modüllerimizi çağırdık 

def puan(x, y): # puan fonksiyonu oluşturduk
    global p 
    p = p+1 
    top.goto(random.randint(-300, 300), random.randint(-300, 300)) 
    

pencere = turtle.Screen() #pencere oluşturuldu
pencere.title('Dikkat Oyunu') # pencere başlığı
pencere.bgcolor('yellow') #pencere rengi
pencere.setup(width=600 , height=600) # pencere boyutları

top = turtle.Turtle() #bir top adında nesne oluşturuldu
top.speed(0) # nesne hareketi 0 olcak animasyonsuz
top.shape('circle') # nesnenin şekli curcle(daire) şenlinde olacağını tanımladık
top.color('black') #nesne rengini kırmızı atadık
top.shapesize(3) #buyukluğunu 3 aldık
top.penup() # herhangi bir çizgi çizmesin diye konumu rastgele yaptık
top.goto(random.randint(-300, 300), random.randint(-300, 300)) #rastgele bir konum ekliyoruz


yaz = turtle.Turtle() # yaz adında yeni nesne oluşturduk
yaz.speed(0)  #nesnenin animasyou olmuycak
yaz.shape('square') # nesne şekli square(kare) olsun
yaz.color('red')  #nesne rengi
yaz.penup() #kaleimi kaldırdık
yaz.goto(0, 260) # yazacaığımız noktaya gidiyoruz
yaz.hideturtle() # kaplumbağayı gizliyoruz
yaz.write('Start' ,align='center', font=('Verdana',24)) # yazının özelliklerini belirttik
 
p=0 #puanı sıfır aldık

sure = 5 #beş saniye sürsi verildi

 
while True:
    baslangicSure = time.time()
    while(time.time() - baslangicSure) < sure:
        top.onclick(puan) # nesne üstüne click yapıldığında oluşacaklar >>> puan oynuycak
    else:    
        yaz.clear() 
        yaz.write('Puan: {}'.format(p), align='center', font=('Verdana', 24))
        time.sleep(2)
        p = 0
        yaz.clear()
        yaz.write('Start', align='center', font=('Verdana', 24))
        
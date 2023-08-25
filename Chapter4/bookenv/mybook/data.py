from chapters.models import Chapter

chapter1 = Chapter(name="Web Scraping", description="Web scraping is a process of extracting and analyzing data from various websites. This can be easy or difficult or even impossible due to legal issues or various methods to prevent web scraping.")

chapter1.save()

chapter2 = Chapter(name="File Parsing", description="Python may be useful for different file formats parsing and conversion. Let’s briefly cover a couple of examples.")

chapter2.save()

chapter3 = Chapter(name="Working with Various APIs", description="API (Application Programming Interface) is a way or protocol defining how different programs can interact with each other. Python is a great tool for dealing with almost every REST (Representational state transfer) API which is the most popular type of API protocol nowadays. It is easy to work with Twitter API, GitHub API and a lot of other APIs using Python.")

chapter3.save()

chapter4 = Chapter(name="Creating Websites", description="Python is widely used in the modern world of web development. There are several popular web frameworks for Python including Django and Flask. In this chapter we will build a very basic website using Django. It will be a website about this book and its chapters.")

chapter4.save()

chapter5 = Chapter(name="Graphs and Data Visualization", description="It is really simple even for absolute beginners to draw plots using Python due to the great plotting library called Matplotlib. Matplotlib together with Numpy (another awesome Python library adding support for arrays and matrices) provides a power comparable to MATLAB which is itself a great computing platform for analyzing data. But Matplotlib is much simpler to use.  Matplotlib has clear and full online documentation so I advise you to go to https://matplotlib.org and browse as many as possible examples there. Here we will discuss some types of graphs including pie and bar charts.")

chapter5.save()

chapter6 = Chapter(name="OpenCV", description="OpenCV stands for Open Source Computer Vision library. It is easy to guess it mainly deals with computer vision but it has very powerful functionality having modules for image processing, video, camera, machine learning and much much more. OpenCV itself is written in C++ and it has bindings for several languages including Python.")

chapter6.save()

chapter7 = Chapter(name="Machine Learning", description="Machine learning and deep learning are among the most popular topics related to computer science today. In this chapter we will briefly discuss machine learning and in the next chapter - deep learning. Machine learning is a very wide topic so we will concentrate only on some Python-related aspects of it.")

chapter7.save()

chapter8 = Chapter(name="Deep Learning", description="Deep learning is a kind of machine learning which we discussed in Chapter 7. The word “deep” means that its architecture has multiple layers (including an input layer, hidden layers and an output layer).")

chapter8.save()

chapter9 = Chapter(name="What Python is Not Good For", description="Throughout this book we have discussed what a great language Python is and how it could be used. But it has its own problems and disadvantages (as any other language, I believe). In this chapter, we will briefly talk about the areas where Python is not so good (or even bad or totally unsuitable).")

chapter9.save()
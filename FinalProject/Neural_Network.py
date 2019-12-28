#Group Member: Yihui A. Wuchen, Xing Yang
#CSC 113 Final Project Neural Network


from random import randint
from random import sample

class neural_network:
  original = {} #this is to keep the original set of all image
  training_set = {} #this use store the trainning set for all image1
  testing_set = {} #this use to store the testing set
  J = [] #this is the index set that indicate the index of the array
  S = [] #this is the value that corresponding to the index that store in J
  T = {} #this use to store the occurance when we are running the trainning set
  n = 3 #this is the default tuple size, this also indicate how many index need to be randomize
  m = 4 #this is the number of sube set that J and T should have
  d = 0 #this is for bonus question.
  len_training_set = 0
  len_testing_set = 0

  def __init__(self, image1, list_image1, image2, list_image2, tuple_size = 3):
    #this is used to initial the variable
    array_size = len(list_image1) #first need to see the array size of image
    if array_size != len(list_image2):
      raise Exception('The length of first image is different the length of second!')
    elif tuple_size <= 0 or tuple_size > array_size or array_size%tuple_size != 0:
      raise Exception('The size of image should be able to divisible by tuple size!')
    self.n = tuple_size
    self.m = int(array_size/tuple_size)
    self.original = {image1 : list_image1, image2 : list_image2} #use to store the original image set
    self.generate_J(array_size) #generate the index set J
    self.generate_T() #generate T

  def convert(self,arr): 
    #convert a binary array that contain 1 or 0 to decimal
    #ex. [1,0,1] will return 5
    if len(arr) == 1:
      return arr[0]
    return self.convert(arr[1:]) * 2 + arr[0]

  def convert_J_to_S(self, image_array, J_subarray):
    #input: image_array is a array that indicate the image. J_subarray is one of the subarray inside the index set J
    #output: return a binary array which can be use to represent S
    tmp = []
    for index in J_subarray:
      tmp.append(image_array[index])
    return tmp

  def generate_T(self):
    #output: generate empty T sets for each image such as H, L or add a new T set for new image
    #the size of T is determined by the m and the size of array inside the T is determined by 2**n since n is the size of index set J 
    size_T = self.m
    size_subarray = 2**self.n
    list_key = self.original.keys()
    list_T_key = self.T.keys() 
    for key in list_key:
      if key in list_T_key: #check if there is a exist key value in T
        pass
      else:
        self.T[key] = []
        for num in range(size_T):
          self.T[key].append([0 for x in range(size_subarray)])

  def generate_J(self, size):
    #input: size is use to determine how many elements inside J
    #output: generate a index set J with random value without any repition
    #the value n is use to determine the size of subarray
    #this function can only run one time
    if len(self.J) != 0:
      raise Exception("the index set J is already implemented")
    J_tmp = sample([x for x in range(0,size)], size)
    i = 0
    while i<size:
      self.J.append(J_tmp[i:i+self.n])
      i+=self.n

  def generate_dataset(self, iteration, File = "dataset.txt"):
    open(File, "w").close()
    self.len_training_set = iteration//2 - 100
    self.len_testing_set = 100
    with open(File, "a") as f:
        for key, value in self.original.items():
            image_index = [x for x in range(self.n * self.m)]
            for num in range(iteration//2):
              random_index = sample(image_index , self.n) #this is use to indicate which index in the image array need to be random
              tmp_list = []
              for index in range(len(value)):
                if index in random_index:
                  f.write(str(randint(0,1)) + " ")
                else:
                  f.write(str(value[index]) + " ")
              f.write("\n")

  def dump_dataset(self, File = "dataset.txt"):
    keys = list(self.original.keys())
    for key in keys:
        self.training_set[key] = []
        self.testing_set[key] = []
    iteration = 0
    image = 0
    tmp_list = []
    with open(File, "r") as f:
        for elem in f.read():
            if elem == "\n":
                iteration += 1
                if iteration > self.len_testing_set + self.len_training_set:
                    image += 1
                    iteration = 1
                if iteration > self.len_training_set:
                    self.testing_set[keys[image]].append(tmp_list)
                else:
                    self.training_set[keys[image]].append(tmp_list)
                tmp_list = []
            else:
                if elem == " ":
                    pass
                else:
                    tmp_list.append(int(elem))
                

  def training(self):
    #this function serve as training the computer to recognize the image
    #we will use the index set J as a index to get S and use S to determine the location of index inside array T 
    for trainning_key, trainning_value in self.training_set.items():
        for tmp_list in trainning_value:
          for index in range(len(self.J)): 
            #run index set J as J1, J2, J3, J4 which indicate which subarray in T
            #should be use. For example, J1 corresponding to T1, J2 corresponding to T2 so on
            self.S = (self.convert_J_to_S(tmp_list, self.J[index]))
            self.T[trainning_key][index][self.convert(self.S)] += 1
  
  def testing(self):
    #this part is use to test if computer recognize the unknown image from testing set
    #we use the index set J and transform it to array S to get the location of the value inside T. 
    #Then, sum them together to compare each image sum to see whoever is bigger
    sum_all_images = {}
    num_true = 0
    num_iteration = 0
    testing_set_used = {"H" : 0 , "L" : 0} #this serve as the number of testing case have been use
    for itera in range(200):
      num_iteration += 1
      if(itera < 100):
          unknown = "H"
      else:
        unknown = "L"
      unknown_image = self.testing_set[unknown][testing_set_used[unknown]]
      testing_set_used[unknown] += 1
      for key in self.original.keys():
        sum_all_images[key] = 0
      for index in range(len(self.J)):
        self.S = (self.convert_J_to_S(unknown_image, self.J[index]))
        for key in sum_all_images.keys():
          sum_all_images[key] += self.T[key][index][self.convert(self.S)]

      max_total = 0 #get the maximun sum of a image
      max_image = "" #get the predict class

      for key, value in sum_all_images.items():
        if value > max_total:
          max_total = value
          max_image = key

      print([unknown_image, "Actual Class:", unknown, "Predicted Class:", max_image, max_image == unknown])
      if (max_image == unknown):
        num_true += 1
        adjust = int(itera*self.d) #Bonus
      else:
        adjust = int(-itera*self.d) #Bonus
      for index in range(len(self.J)): #Bonus
        self.S = (self.convert_J_to_S(unknown_image, self.J[index])) #Bonus
        self.T[max_image][index][self.convert(self.S)] += adjust #Bonus
      print("Accuracy:", str(int((num_true*100)/num_iteration)) + "%\n")


def main():
  H = [1,0,1,1,1,1,1,1,1,1,0,1]
  L = [1,0,0,1,0,0,1,0,0,1,1,1]
  try:
      datasize = 800
      test = neural_network('H', H, 'L', L)
      test.generate_dataset(datasize)
      print("length of training case:", test.len_training_set)
      print("length of testing case:", test.len_testing_set, "\n")
      test.dump_dataset()
      test.training()
      test.testing()
  except:
      print("some error")

main()

import pickle

# x = 10
# y = [1, 2, 3, 4]

# serialization
# with open("pickle_file", mode="wb") as p_file:

#     # 存進去
#     pickle.dump(x, p_file)
#     pickle.dump(y, p_file)

# de-serialization
# with open("pickle_file", mode="rb") as p_file:

#     # 拿出來
#     print(pickle.load(p_file))
#     print(pickle.load(p_file))


# practical
# serialization data
# x = 10
# y = 20
# my_list = [1, 2, 3]


# def save_data():
#     global x, y, my_list
#     data = {"x": x, "y": y, "my_list": my_list}
#     with open("my_pickle_file", mode="wb") as pfile:
#         # 將 data 存到 pfile
#         pickle.dump(data, pfile)


# save_data()


x = None
y = None
my_list = None


def restore_data():
    global x, y, my_list
    with open("my_pickle_file", mode="rb") as pfile:
        data = pickle.load(pfile)
        x = data["x"]
        y = data["y"]
        my_list = data["my_list"]


restore_data()
print(x, y, my_list)
# 10 20 [1, 2, 3]

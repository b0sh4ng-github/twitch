import sys
import pickle

userlogin = pickle.load( open( sys.argv[1] + ".pickle", "rb" ) )

print(userlogin)
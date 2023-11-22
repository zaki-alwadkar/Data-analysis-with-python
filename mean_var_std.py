def calculate(lst):
  import numpy as np
  if len(lst) != 9:
    raise ValueError("List must contain nine numbers.")
  x = np.array(lst).reshape(3, 3)
  result = {
      k: [func(x, axis=ax).tolist() for ax in [0, 1, None]]
      for (k, func) in
      zip(["mean", "variance", "standard deviation", "max", "min", "sum"],
          [np.mean, np.var, np.std, np.amax, np.amin, np.sum])
  }
  return result

import torch 
import logging 

def model(t_u, w, b): 
    """
    Returns a tensor of predicted values using the inputs in a linear model. 
    t_u: Dependent variable. Input Tensor. Data we will use to predict the output t_c 
    w: Weight parameter. PyTorch scalar (zero-dimensional tensor)
    b: Bias parameter (Offset parameter). The bias is what the output would be if all the inputs were zero. 
    """
    return w * t_u + b

def loss_fn(t_p, t_c): 
    """
    Mean square loss function. 
    t_p: predicted value
    t_c: actual value


    """
    squared_diffs = (t_p-t_c)**2
    return squared_diffs.mean() 

def main(): 
    t_c = [0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0]
    t_u = [35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4]
    t_c = torch.tensor(t_c) #celcius temps 
    t_u = torch.tensor(t_u) #unknown unit

    # Track the entire family tree of tensors resulting from operations on params using `requires_grad=True`
        # Any tensor that has params as an ancestor will have access to the chain of functions that were called on it.
            # In the case that the functions are differentiable, 
            # the value of the derivative will be automatically populated as a grad attr. of the params tensor

    params = torch.tensor([1.0,0.0], requires_grad=True)
    loss = loss_fn(model(t_u, *params), t_c)
    loss.backward()

    return print(params.grad) 


if __name__ =="__main__":
    main() 
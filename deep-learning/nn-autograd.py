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

def training_loop(n_epochs, learning_rate, params, t_u, t_c):
    for epoch in range(1, n_epochs + 1):

        if params.grad is not None: 
            params.grad.zero_()

        t_p=model(t_u, *params)
        loss = loss_fn(t_p, t_c)
        loss.backward() 

        with torch.no_grad():
            params -= learning_rate * params.grad

        if epoch % 500 == 0: 
            print(f'Epoch {epoch}, Loss {float(loss)}')
    return params

def main(): 
    t_c = torch.tensor([0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0])
    t_u = torch.tensor([35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4])
    t_un = t_u*.1
    # Track the entire family tree of tensors resulting from operations on params: `requires_grad=True`
        # Any tensor that has params as an ancestor will have access to the chain of functions that were called on it.
            # In the case that the functions are differentiable, 
            # the value of the derivative will be automatically populated as a grad attr. of the params tensor
    params = training_loop(
        n_epochs = 5000,
        learning_rate = 1e-2,
        params = torch.tensor([1.0,0.0], requires_grad=True),
        t_u = t_un,
        t_c = t_c
    )
    return print(params.grad) 


if __name__ =="__main__":
    main() 
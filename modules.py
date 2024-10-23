import torch
import torch.nn as nn



class Yolov7(nn.Module):
    def __init__(self, weights_path='C:/Users/Administrator/Documents/PatternAnalysis-2024/recognition/yolov7/yolov7.pt'):
        super(Yolov7, self).__init__()
        print("Initializing YOLOv7 model")
        
        # Load model weights
        self.model = torch.hub.load("WongKinYiu/yolov7", "custom", weights_path, trust_repo=True)
        
        
        # Move model to device
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)


    def forward(self, images):
        with torch.no_grad():
            results = self.model(images)
        return results
    
model = Yolov7()
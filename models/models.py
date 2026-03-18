import os

project_folder_path = os.path.dirname(os.path.abspath(__file__))
project_folder_path = os.path.join(project_folder_path, "..")
data_folder = os.path.join(project_folder_path, "data")
output_folder = os.path.join(project_folder_path, "output")
save_folder = os.path.join(project_folder_path, "savedModels")

def create_model(opt):
    if(opt['model'] == "splats"):
        from models.PeriodicPrimitives2D import PeriodicPrimitives2D
        return PeriodicPrimitives2D(opt)
    elif(opt['model'] == "iNGP"):
        from models.iNGP import iNGP
        return iNGP(opt)
    
def load_model(opt, location):
    if(opt['model'] == "splats"):
        from models.PeriodicPrimitives2D import PeriodicPrimitives2D
        model = PeriodicPrimitives2D(opt)
    elif(opt['model'] == "iNGP"):
        from models.iNGP import iNGP
        model = iNGP(opt)
    model.load(location)
    return model
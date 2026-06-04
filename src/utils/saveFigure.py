
import matplotlib.pyplot as plt
from src.config import OUTPUT_DIR

def saveFigure(filename: str, fig=None):
    """
    Saves a matplotlib/seaborn figure to the output/figures directory.
    
    Parameters:
    filename (str): Name of the file (e.g., 'inflation_trend.png')
    fig (matplotlib.figure.Figure): Optional figure object. 
                                    If None, saves the active figure.
    """
    # 1. Define the output target directory relative to your PROJECT_ROOT
    output_dir = OUTPUT_DIR / 'figures'
    
    # 2. Automatically create folders if they don't exist yet
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. Create the absolute final path for the file
    save_path = output_dir / filename
    
    # 4. If no specific figure was passed, fetch the currently active one
    if fig is None:
        fig = plt.gcf()  # gcf = Get Current Figure
        
    # 5. Save the image cleanly
    fig.savefig(
        save_path, 
        dpi=300,              # Professional publication resolution 
        bbox_inches='tight',  # Automatically clips extra margins so text doesn't get cut off
        facecolor='white'     # Forces a clean solid white background
    )
    print(f"✅ Figure successfully saved to: {save_path}")
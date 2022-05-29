import matplotlib.pyplot as plt
import pandas as pd

def style():
    fig=plt.figure(figsize =(10, 7))
    fig.patch.set_facecolor("#00ffff")
    ax = fig.add_subplot(1, 1, 1)
    ax.set_facecolor("#00ffff")
    plt.grid(axis="y",color="#abe1e1",linewidth=0.7)
    ax.set_frame_on(False)
    return fig,ax

def plot_comparision_of_genome_accuracy():
    fig,ax=style()
    df = pd.DataFrame(pd.read_excel("comparision_of_genome_accuracy.xlsx"))
    plt.ylim(0.8,0.96)
    title = df['Title'][0]
    x_axis_name=df['Xlabel'][0]
    y_axis_name=df.columns[-1]
    x_axis_label1=df.columns[2]
    x_axis_label2=df.columns[3]
    x_axis_label3=df.columns[4]
    x_axis_values1=df[x_axis_label1]
    x_axis_values2=df[x_axis_label2]
    x_axis_values3=df[x_axis_label3]
    y_axis_values=df[y_axis_name]
    
    plt.plot(y_axis_values,x_axis_values1,marker="o", color ="#4472c4",zorder=3,label=x_axis_label1)
    plt.plot(y_axis_values,x_axis_values2,marker="o", color ="#a5a5a5",zorder=3,label=x_axis_label2)
    plt.plot(y_axis_values,x_axis_values3,marker="o", color ="#ed7d31",zorder=3,label=x_axis_label3)

 
    plt.xlabel(x_axis_name,fontweight='bold')
    plt.ylabel(y_axis_name,fontweight='bold')
    plt.title(title,fontweight='bold')
    ax.legend(loc='upper center',ncol=3, bbox_to_anchor=(0.5, -0.08),facecolor="#00ffff",frameon=False)
    plt.show()

def plot_comparision_of_genome_training():
    fig,ax=style()
    df = pd.DataFrame(pd.read_excel("comparision_of_genome_training.xlsx"))
    plt.ylim(0,4000)
    title = df['Title'][0]
    x_axis_name=df['Xlabel'][0]
    y_axis_name=df.columns[-1]
    x_axis_label1=df.columns[2]
    x_axis_label2=df.columns[3]
    x_axis_values1=df[x_axis_label1]
    x_axis_values2=df[x_axis_label2]
    y_axis_values=df[y_axis_name]
    
    plt.bar(y_axis_values-0.2, x_axis_values1, color ="#4472c4",
        width = 0.3,zorder=3,label=x_axis_label1)
    plt.bar(y_axis_values+0.2, x_axis_values2, color ="#ed7d31",
        width = 0.3,zorder=3,label=x_axis_label2)

 
    plt.xlabel(x_axis_name,fontweight='bold')
    plt.ylabel(y_axis_name,fontweight='bold')
    plt.title(title,fontweight='bold')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08),facecolor="#00ffff",frameon=False, ncol=2)
    plt.show()

def plot_comparision_of_bin_training():
    fig,ax=style()
    df = pd.DataFrame(pd.read_excel("comparision_of_bin_training.xlsx"))
    plt.ylim(0,60000)
    title = df['Title'][0]
    x_axis_name=df['Xlabel'][0]
    y_axis_name=df.columns[-1]
    x_axis_label1=df.columns[2]
    x_axis_label2=df.columns[3]
    x_axis_values1=df[x_axis_label1]
    x_axis_values2=df[x_axis_label2]
    y_axis_values=df[y_axis_name]
    
    plt.bar(y_axis_values-0.2, x_axis_values1, color ="#4472c4",
        width = 0.3,zorder=3,label=x_axis_label1)
    plt.bar(y_axis_values+0.2, x_axis_values2, color ="#ed7d31",
        width = 0.3,zorder=3,label=x_axis_label2)

 
    plt.xlabel(x_axis_name,fontweight='bold')
    plt.ylabel(y_axis_name,fontweight='bold')
    plt.title(title,fontweight='bold')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08),facecolor="#00ffff",frameon=False, ncol=2)
    plt.show()

def plot_comparision_of_algorithm_accuracy():
    fig,ax=style()
    df = pd.DataFrame(pd.read_excel("comparision_of_algorithm_accuracy.xlsx"))
    plt.ylim(0.8,0.96)
    title = df['Title'][0]
    x_axis_name=df['Xlabel'][0]
    y_axis_name=df.columns[-1]
    x_axis_label=df.columns[2]
    x_axis_values=df[x_axis_label]
    y_axis_values=df[y_axis_name]
    
    plt.bar(x_axis_values, y_axis_values, color ="#4472c4",
        width = 0.4,zorder=3,label=x_axis_label)

 
    plt.xlabel(x_axis_name,fontweight='bold')
    plt.ylabel(y_axis_name,fontweight='bold')
    plt.title(title,fontweight='bold')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08),facecolor="#00ffff",frameon=False)
    plt.show()

if __name__ == '__main__':    
    plot_comparision_of_algorithm_accuracy()
    plot_comparision_of_genome_accuracy()
    plot_comparision_of_genome_training()
    plot_comparision_of_bin_training()
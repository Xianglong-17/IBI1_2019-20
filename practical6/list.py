#sort the list and remove the last number
#reverse and remove the last number
#print list
gene_lengths = [9410,3944141,4442,105338,19149,76779,126550,36296,842,15,981]
gene_lengths.sort()
gene_lengths.pop()
gene_lengths.reverse()
gene_lengths.pop()
gene_lengths.reverse()
print(gene_lengths)

#create the chart
import matplotlib.pyplot as plt
score= gene_lengths
plt.boxplot(score,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps = True,
            showfliers=True,
            notch=False
            )
plt.show()
from matplotlib import pyplot as plt
import pandas as pd

species = pd.read_csv('species_info.csv')
print(species.head())

species.fillna('No Intervention', inplace=True)
protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name').reset_index(drop=True)
print(protection_counts)

plt.figure(figsize = (10, 4))
ax = plt.subplot()

plt.bar(range(len(protection_counts)), protection_counts.scientific_name)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
plt.show()

species['is_protected'] = species.apply(lambda row: True if row['conservation_status'] != 'No Intervention' else False, axis=1)
category_counts = species.groupby(['category', 'is_protected']).scientific_name.nunique().reset_index()
category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()
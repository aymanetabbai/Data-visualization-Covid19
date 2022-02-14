# -*- coding: utf-8 -*-
"""
Created on Sat May  8 22:32:48 2021

@author: hassi
"""
import LoadData as l
import numpy as np
np.random.seed(42)
import matplotlib.pyplot as plt


def euclidean_distance(x1,x2) :
    return np.sqrt(np.sum(x1-x2)**2)

class KMeans  :
    def __init__(self,K,max_iteration=100,graph=False) :
        
        self.K=K
        self.max_iteration=max_iteration
        self.graph=graph
        self.clusters=[[] for _ in range(self.K)] #list des clusters
        self.centroids=[] #list des centre de chaque cluster
        
    def predict(self,X) :
        self.X=X
        self.n_samples,self.n_features=X.shape
        #initialisation des centroids 
        random_sample_idxs=np.random.choice(self.n_samples,self.K,replace=False)
        self.centroids=[self.X[idx] for idx in random_sample_idxs
                                               
                        ]
        #algorithme d'iteration
        for _ in range (self.max_iteration) :
            
            # mise à jour des clusters
            self.clusters=self.create_clusters(self.centroids)
            if self.graph :
                self.plot()
            #mise à jour des centroids
            centroids_old= self.centroids
            self.centroids=self.get_centroids(self.clusters)
            if self.graph:
                
                self.plot()
            #verifier si l'algorithmle converge 
            if self.is_converged(centroids_old,self.centroids) :
                break
        #return les clusters 
        return self.get_cluster_labels(self.clusters)
    
    def get_cluster_labels(self,clusters) :
        labels=np.empty(self.n_samples)
        for cluster_idx , cluster in enumerate(clusters) :
            for sample_idx in cluster :
                labels[sample_idx]=cluster_idx
        return labels
    
    def create_clusters(self,centroids) :
        clusters=[[] for _ in range (self.K)]
        for idx , sample in enumerate(self.X) : 
            centroid_idx=self.closest_centroid(sample,centroids)
            clusters[centroid_idx].append(idx)
        return clusters
    
    def closest_centroid(self,sample,centroids) :
        distances=[euclidean_distance(sample, point) for point in centroids]
        closest_idx=np.argmin(distances)
        return closest_idx
    
    def get_centroids(self,clusters) :
        centroids=np.zeros((self.K,self.n_features))
        for cluster_idx,cluster in enumerate(clusters) :
            cluster_mean=np.mean(self.X[cluster],axis=0)
            centroids[cluster_idx]=cluster_mean
        return centroids
    def is_converged(self,centroids_old,centroids) :
        distances=[euclidean_distance(centroids_old[i],centroids[i]) for i in range (self.K)]
        return sum(distances)==0
        
    def plot(self) :
        
        fig,ax=plt.subplots(figsize=(12,8))
        
        for i,index in enumerate(self.clusters) :
            point=self.X[index].T
            ax.scatter(*point)
        
        for point in self.centroids :
            ax.scatter(*point,marker="x",color="black",linewidth=2)
        plt.show()
        


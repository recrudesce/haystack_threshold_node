from haystack.schema import Document
from typing import Optional, List, Dict, Tuple, Optional
from haystack.nodes.base import BaseComponent

class DocumentThreshold(BaseComponent):
    def __init__(self,
                threshold: Optional[int] = 75,
                ):
        """
        This component filters documents based on a threshold percentage, ensuring only the 
        documents above the threshold get passed down the pipeline.
        :param threshold: The threshold to use for filtering documents in whole numbers (81 = 81%).
        """
    
        super().__init__()
        self.threshold = float(threshold/100)
        
    outgoing_edges = 1

    def run(self, documents: List[Document]) -> Tuple[Dict, str]:
        return {"documents": [x for x in documents if x.score > self.threshold]}, "output_1"
    
    def run_batch(self, results, **kwargs):
        pass
from langchain_community.tools.tavily_search import TavilySearchResults

def get_tools(enable:bool):
    if enable:
        return [TavilySearchResults(
            max_results=3,  # Increased from 2 to get more context
            include_domains=["news", "blogs", "wikipedia"],  # Focus on current information sources
            search_depth="advanced"  # Get more comprehensive results
        )]
    return []
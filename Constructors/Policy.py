from Constructors.Multilabel import *

class Policy:
    def __init__(self, patterns):
        self.patterns = patterns

    def get_pattern_sink(self, sink):
        patterns_sink=[]
        for pattern in self.patterns:
            if pattern.is_sink(sink):
                patterns_sink += [pattern]
        return patterns_sink

    def get_all_vulnerabilities(self):
        return [pattern.get_vulnerability_name() for pattern in self.patterns]
    
    def get_all_sources(self):
        sources = []
        for pattern in self.patterns:
            sources += pattern.get_source_names()
        return sources

    def get_all_sinks(self):
        sinks = []
        for pattern in self.patterns:
            sinks += pattern.get_sink_names()
        return sinks
    
    def get_patterns_for_source(self, source):
        patterns = []
        for pattern in self.patterns:
            if source in pattern.get_source_names():
                patterns += [pattern]
        return patterns

    def get_sources_for_vulnerability(self, vulnerability_name):
        sources = [pattern.source_names for pattern in self.patterns if pattern.vulnerability_name == vulnerability_name]
        return sources[0] if sources else []

    def get_sanitizers_for_vulnerability(self, vulnerability_name):
        sanitizers = [pattern.sanitizer_names for pattern in self.patterns if pattern.vulnerability_name == vulnerability_name]
        return sanitizers[0] if sanitizers else []

    def get_sinks_for_vulnerability(self, vulnerability_name):
        sinks = [pattern.sink_names for pattern in self.patterns if pattern.vulnerability_name == vulnerability_name]
        return sinks[0] if sinks else []

    def illegal_flows_for_program_counter(self, name, multilabel):
        illegal_multilabel = Multilabel([])

        for pattern in self.patterns:
            if name in pattern.sink_names and multilabel.has_source(pattern.source_names):
                illegal_multilabel.pattern_labels[pattern.vulnerability_name] = multilabel.pattern_labels[pattern.vulnerability_name]

        return illegal_multilabel
    
    def get_illegal_flows(self, name: str, multilabel: Multilabel, implicit: bool = False) -> Multilabel:
        illegal_flows_multilabel = Multilabel([])
        print("\n\n\n")
        print(multilabel)
        pattern_labels = multilabel.pattern_labels
        print("name:", name) # check if pattern_labels has stuff like {str , label}
        print(pattern_labels.keys())
        for pattern in pattern_labels.keys():
            if pattern.is_sink(name) and not (not pattern.implicit and implicit):
                #print(f"Found illegal flow for pattern {pattern.vulnerability}")
                illegal_flows_multilabel.update({pattern: pattern_labels[pattern]})
        
        return illegal_flows_multilabel
    
    def add_pattern(self, pattern):
        self.patterns += [pattern]

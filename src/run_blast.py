from Bio.Blast import NCBIWWW, NCBIXML

def blast_sequence(seq_record, output_xml_path):
    result_handle = NCBIWWW.qblast("blastn", "nt", seq_record.seq)
    with open(output_xml_path, "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

def parse_blast_result(xml_path):
    with open(xml_path) as result_handle:
        blast_record = NCBIXML.read(result_handle)
        summary = []
        for alignment in blast_record.alignments[:5]:
            for hsp in alignment.hsps:
                summary.append({
                    "title": alignment.title,
                    "length": alignment.length,
                    "e_value": hsp.expect,
                    "score": hsp.score
                })
        return summary

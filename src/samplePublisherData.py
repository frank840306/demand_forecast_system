

def sampleData():
	publisher = {
		'publisher_A' : {
			'book_1' : { 
				'name' : 'Recrystallization and Related Annealing Phenomena',
				'id' : 616,
				'author' : 1,
				'type' : 'Chemical Engineering',
				'price' : 10.49,
				'dollar' : 'USD',
				'description' : 'Theory of Electrophoresis and Diffusiophoresis of Highly Charged Colloidal Particles investigates the electrophoretic and diffusiophoretic behaviors of highly charged particles with theoretical approaches by rigorously solving the complete general electrokinetic equations numerically, without any simplifications or approximations. It examines in detail the features that are pertinent to highly charged particles. Special attention is given to the polarization effect that is by far the most important one. This book provides realistic predictions for the electrophoretic mobility of highly charged particles such as proteins and DNAs, which are of great interest in the field of biochemistry and biomedical applications. Further this book provides extensive treatments of the non-rigid colloidal systems of practical interests such as the liquid droplets, pores, porous systems and gels, in addition to the convectional rigid particles. As a result, it serves as a very useful tool for chemical engineers or research scientists by providing easy-to-apply charts to either interpret their experimental data or explore feasibility of novel designs in practical operations.',
				'link' : 'https://www.elsevier.com/books/recrystallization-and-related-annealing-phenomena/rollett/978-0-08-044164-1'
			},
			'book_2' : {
				'name' : 'The Human Body',
				'id' : 517,
				'author' : 3,
				'type' : 'Biochemistry, Genetics and Molecular Biology',
				'price' : 19.99,
				'dollar' : 'USD',
				'description' : 'No one explains A&P more clearly! The Human Body in Health & Disease, 7th Edition makes it easier to understand how the body works, both in normal conditions and when things go wrong. Its easy-to-read writing style, more than 500 full-color illustrations, and unique Clear View of the Human Body transparencies keep you focused on the principles of anatomy, physiology, and pathology. New to this edition are Connect It! features with bonus online content and concept maps with flow charts to simplify complex topics. From noted educators Kevin Patton and Gary Thibodeau, this book presents A&P in a way that lets you know and understand what is important.',
				'link' : 'https://www.elsevier.com/books/the-human-body-in-health-and-disease-softcover/patton/978-0-323-40211-8'
			},
			'book_3' : {# in the Pathogenesis of Pulmonary Disease
				'name' : 'Lung Epithelial Biology',
				'id' : 559,
				'author' : 88,
				'type' : 'Biomedical Science and Medicine',
				'price' : 13.99,
				'dollar' : 'USD',
				'description' : 'Lung Epithelial Biology in the Pathogenesis of Pulmonary Disease provides a one-stop resource capturing developments in lung epithelial biology related to basic physiology, pathophysiology, and links to human disease. The book provides access to knowledge of molecular and cellular aspects of lung homeostasis and repair, including the molecular basis of lung epithelial intercellular communication and lung epithelial channels and transporters. Also included is coverage of lung epithelial biology as it relates to fluid balance, basic ion/fluid molecular processes, and human disease. Useful to physician and clinical scientists, the contents of this book compile the important and most current findings about the role of epithelial cells in lung disease. Medical and graduate students, postdoctoral and clinical fellows, as well as clinicians interested in the mechanistic basis for lung disease will benefit from the books examination of principles of lung epithelium functions in physiological condition.',
				'link' : 'https://www.elsevier.com/books/lung-epithelial-biology-in-the-pathogenesis-of-pulmonary-disease/sidhaye/978-0-12-803809-3'
			},
			# 'book_num' : 3
		},
		'publisher_B' : {
			'book_4' : {
				'name' : 'Case Studies in Public Health',
				'id' : 568,
				'author' : 2,
				'type' : 'Biomedical Science and Medicine',
				'price' : 16.49,
				'dollar' : 'USD',
				'description' : 'Case Studies in Public Health contains selected case studies of some of the most important and influential moments in medicine and epidemiology. The cases chosen for this collection represent a wide array of public health issues that go into the makeup of what can be termed the New Public Health (NPH), which includes traditional public health, such as sanitation, hygiene and infectious disease control, but widens its perspective to include the organization, financing and quality of health care services in a much broader sense. Each case study is presented in a systematic fashion to facilitate learning, with the case, background, current relevance, economic issues, ethical issues, conclusions, recommendation and references discussed for each case. The book is a valuable resource for advanced students and researchers with specialized knowledge who need further information on the general background and history of public health and important scientific discoveries within the field. It is an ideal resource for students in public health, epidemiology, medicine, anthropology, and sociology, and for those interested in how to apply lessons from the past to present and future research.',
				'link' : 'https://www.elsevier.com/books/case-studies-in-public-health/tulchinsky/978-0-12-804571-8'
			},
			'book_5' : {
				'name' : 'Earth\'s Oldest Rocks',
				'id' : 751, 
				'author' : 16,
				'type' : 'Earth and Planetary Sciences',
				'price' : 5.99,
				'dollar' : 'USD',
				'description' : 'Earth\’s Oldest Rocks provides a comprehensive overview of \
all aspects of early Earth, from planetary accretion through to development \
of protocratons with depleted lithospheric keels by c. 3.2 Ga, in a series of \
papers written by over 50 of the world\'s leading experts. The book is divided \
into two chapters on early Earth history, ten chapters on the geology of specific \
cratons, and two chapters on early Earth analogues and the tectonic framework \
of early Earth. Individual contributions address topics that range from planetary \
accretion, a review of Earth meteorites, significance and composition of Hadean \
protocrust, composition of Archaean mantle and deep crust, all aspects of the geology \
of Paleoarchean cratons, composition of Archean oceans and hydrothermal environments, \
evidence and geological settings of early life, early Earth analogues from Venus \
and New Zealand, and a tectonic framework for early Earth.',
				'link' : 'https://www.elsevier.com/books/earths-oldest-rocks/van-kranendonk/978-0-444-52810-0'
			},
			'book_6' : {
				'name' : 'Algal Green Chemistry',
				'id' : 663,
				'author' : 3,
				'type' : 'Chemical Engineering',
				'price' : 15.99,
				'dollar' : 'USD',
				'description' : 'Algal Green Chemistry: Recent Progress in Biotechnology presents \
emerging information on green algal technology for the production of diverse chemicals, \
metabolites, and other products of commercial value. This book describes and emphasizes \
the emerging information on green algal technology, with a special emphasis on the \
production of diverse chemicals, metabolites, and products from algae and cyanobacteria. \
Topics featured in the book are exceedingly valuable for researchers and scientists \
in the field of algal green chemistry, with many not covered in current academic studies. \
It is a unique source of information for scientists, researchers, and biotechnologists \
who are looking for the development of new technologies in bioremediation, eco-friendly \
and alternative biofuels, biofertilizers, biogenic biocides, bioplastics, cosmeceuticals, \
sunscreens, antibiotics, anti-aging, and an array of other biotechnologically important \
chemicals for human life and their contiguous environment. This book is a great asset for \
students, researchers, and biotechnologists.',
				'link' : 'https://www.elsevier.com/books/algal-green-chemistry/rastogi/978-0-444-63784-0'
			},
			'book_7' : {
				'name' : 'CUDA Programming',
				'id' : 730,
				'author' : 1,
				'type' : 'Computer Science',
				'price' : 9.99,
				'dollar' : 'USD',
				'description' : 'If you need to learn CUDA but don\'t have experience \
with parallel computing, CUDA Programming: A Developer\'s Introduction \
offers a detailed guide to CUDA with a grounding in parallel fundamentals. \
It starts by introducing CUDA and bringing you up to speed on GPU parallelism \
and hardware, then delving into CUDA installation. Chapters on core concepts \
including threads, blocks, grids, and memory focus on both parallel and \
CUDA-specific issues. Later, the book demonstrates CUDA in practice for optimizing \
applications, adjusting to new hardware, and solving common problems.',
				'link' : 'https://www.elsevier.com/books/cuda-programming/cook/978-0-12-415933-4'
			},
			# 'book_num' : 4
		},
		'publisher_C' : {
			'book_8' : {
				'name' : 'Process Control',
				'id' : 510,
				'author' : 1,
				'type' : 'Agricultural, Biological, and Food Sciences',
				'price' : 9.59,
				'dollar' : 'USD',
				'description' : 'Instrument Engineers\' Handbook, Third Edition: Process Control \
provides information pertinent to control hardware, including transmitters, \
controllers, control valves, displays, and computer systems. This book presents \
the control theory and shows how the unit processes of distillation and chemical \
reaction should be controlled. Organized into eight chapters, this edition begins \
with an overview of the method needed for the state-of-the-art practice of process \
control. This text then examines the relative merits of digital and analog displays \
and computers. Other chapters consider the basic industrial annunciators and \
other alarm systems, which consist of multiple individual alarm points that are \
connected to a trouble contact, a logic module, and a visual indicator. This book \
discusses as well the data loggers available for process control applications. The \
final chapter deals with the various pump control systems, the features and designs \
of variable-speed drives, and the metering pumps.',
				'link' : 'https://www.elsevier.com/books/process-control/liptak/978-0-7506-2255-4'
			},
			'book_9' : {
				'name' : 'Coding and Decoding: Seismic Data',
				'id' : 786,
				'author' : 77,
				'type' : 'Earth and Planetary Sciences',
				'price' : 4.99,
				'dollar' : 'USD',
				'description' : 'Currently, the acquisition of seismic surveys is performed \
as a sequential operation in which shots are computed separately, one after \
the other. This approach is similar to that of multiple-access technology, \
which is widely used in cellular communications to allow several subscribers \
to share the same telephone line. The cost of performing various shots \
simultaneously is almost identical to that of one shot; thus, the savings in \
time and money expected from using the multishooting approach for computing \
seismic surveys compared to the current approach are enormous. By using this \
approach, the long-standing problem of simulating a three-dimensional seismic \
survey can be reduced to a matter of weeks and not years, as is currently the case.',
				'link' : 'https://www.elsevier.com/books/coding-and-decoding-seismic-data/ikelle/978-0-08-045159-6'
			},
			# 'book_num' : 2
		},
		# 'publisher_num' : 3
	}
	return publisher
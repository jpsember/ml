
rule '.pdf' => '.dot' do |t|
  system("dot -o#{t.name} -Tpdf #{t.source}")
end

desc "Compile dot files to pdf"
task :default => FileList.new("**/*.dot").map{|x| x.chomp("dot") + "pdf"}
